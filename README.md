# TMDB Movie Scraper
Este é um web scraper que extrai informações de filmes da API do The Movie Database (TMDB). </br>

O programa principal consulta a API do TMDB para obter informações sobre filmes com base em seus IDs. Os dados são então salvos em um arquivo CSV. </br>

## Funcionalidades
 - Consulta a API do TMDB para obter informações sobre filmes com base em seus IDs.
 - Salva os dados extraídos em um arquivo CSV.

## Como usar
     - Clone o repositório.
     - Instale as dependências usando o comando pip install -r requirements.txt.
     - Defina sua chave de API do TMDB no arquivo .env como API_KEY=your_api_key. Se você não tiver uma chave de API, registre-se no site do TMDB para obter uma.
     - Execute o arquivo tmdb_movie_scrapper para iniciar o processo de extração de dados. Defina o n° (n) de registros que você quer coletar, default n = 300
     - Aguarde até que todos os filmes sejam processados e os dados sejam salvos no arquivo output/data.csv.

## Tecnologias utilizadas
     - bibliotecas built-in
     - tmdbsimple: Uma biblioteca Python para interagir com a API do TMDB.
     - dotenv: Biblioteca Python para carregar variáveis de ambiente a partir de um arquivo .env.

## Contribuindo
Envie um e-mail para davimmilhome@gmail.com com sua intenção de contribuição que poderei avaliar.

## Autores
Davi Martins Milhome.

## Proximos passos
Adicionar testes unitários.


