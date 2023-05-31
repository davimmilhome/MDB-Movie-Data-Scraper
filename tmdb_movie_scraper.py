"""
Este script realiza requisições à API do TMDB (The Movie Database) para
obter informações de filmes e salvar os dados em um arquivo CSV.

Requerimentos:
- A chave de API do TMDB deve ser fornecida no arquivo
.env como uma variável de ambiente chamada API_KEY.

Funcionalidades:
- O script faz requisições dos N primeiros filmes
- O script utiliza multiprocessing para requisições em paralelo
- A data é salva em CSV, com os campos especificados em 'campos'.
- Caso o arquivo de saída já exista
"""
import csv
import os
from multiprocessing import Pool

from dotenv import load_dotenv
import tmdbsimple as tmdb
import requests

load_dotenv()
tmdb.API_KEY = os.getenv("API_KEY")

n = 300

campos = {
    'base_uri': 'base_uri',
    'session': 'session',
    'timeout': 'timeout',
    'id': 'id',
    'adult': 'adult',
    'backdrop_path': 'backdrop_path',
    'belongs_to_collection': 'belongs_to_collection',
    'budget': 'budget',
    'genres': 'genres',
    'homepage': 'homepage',
    'imdb_id': 'imdb_id',
    'original_language': 'original_language',
    'original_title': 'original_title',
    'overview': 'overview',
    'popularity': 'popularity',
    'poster_path': 'poster_path',
    'production_companies': 'production_companies',
    'production_countries': 'production_countries',
    'release_date': 'release_date',
    'revenue': 'revenue',
    'runtime': 'runtime',
    'spoken_languages': 'spoken_languages',
    'status': 'status',
    'tagline': 'tagline',
    'title': 'title',
    'video': 'video',
    'vote_average': 'vote_average',
    'vote_count': 'vote_count',
}

def get_movie(i):
    """
    Realiza uma requisição à API do TMDB

    :param i: O ID do filme a ser consultado
    :return: Um dicionário com os dados do filme, ou None se erro
    """
    try:
        tmdb.REQUESTS_TIMEOUT = 1
        tmdb.REQUESTS_SESSION = requests.Session()
        movie = tmdb.Movies(i)
        response = movie.info()
        return response

    except Exception as e:
        print(f"Erro ao obter informações do filme {i}: {e}")
        return None

def process_movie(i):
    """
    Processa as informações de um filme obtidas da API do TMDB.

    :param i: O ID do filme a ser processado.
    :return: Um dicionário com os dados do filme processado, ou None
    """
    movie_response = get_movie(i)
    if movie_response:
        row = {}
        for campo, chave in campos.items():
            valor = movie_response.get(chave, '')
            row[campo] = valor

        title = row.get('title', 'N/A')
        print(f"O título do filme na iteração {i} é: {title}")
        return row
    return None

def make_request(i):
    """
    Realiza as requisições à API do TMDB para obter informações dos
    filmes e salva os dados em um arquivo CSV.

    :param i: O número total de filmes a serem consultados.
    """
    arquivo_csv = 'output/data.csv'
    if os.path.exists(arquivo_csv):
        os.remove(arquivo_csv)

    with open(arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=campos.keys())
        writer.writeheader()

        # Cria um pool de processos com o número de processos
        pool = Pool(processes=4)  #

        # Executa as requisições em paralelo usando o pool de processos
        results = pool.map(process_movie, range(1, i + 1))

        # Escreve as linhas válidas no arquivo CSV
        for row in results:
            if row:
                writer.writerow(row)


if __name__ == '__main__':
    make_request(n)

