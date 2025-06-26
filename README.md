
# Desafio Python Revio

## Contexto

Suponha que você seja um desenvolvedor em uma empresa que compra e revende geladeiras. Seu chefe pediu para criar um scraping baseado no e-commerce da Revio, com o objetivo de obter informações para análise de mercado.

## Objetivo

Desenvolver um scraping em Python utilizando o framework **BeautifulSoup** (as dependências estão no arquivo `requirements.txt`) e criar métodos/funções acessíveis via API construída com **FastAPI**. Essas funções devem fornecer as seguintes análises:

### Estrutura dos Produtos

Cada produto deve ser estruturado da seguinte forma nas consultas:

- **nome:** `str`
- **nota:** `float`
- **valor:** `float`

### Funcionalidades da API

1. **Pesquisa direta por nome do produto**  
   Retorna todas as informações relacionadas a um produto com base no seu nome.

2. **Pesquisa por intervalo de valor**  
   Recebe dois valores (mínimo e máximo) para o preço e retorna todos os produtos dentro desse intervalo.

3. **Pesquisa por intervalo de nota**  
   Recebe dois valores (mínimo e máximo) para a nota e retorna todos os produtos dentro desse intervalo.

## Exemplos

- No diretório `/exemplos` há um arquivo chamado `codigo_de_exemplo.py`, que demonstra como interagir com o HTML da página utilizando BeautifulSoup.
- No diretório `/api` há um exemplo de construção de endpoint com FastAPI.

Para rodar a API, execute o comando:

```bash
uvicorn api.app:app --reload
```

Você poderá testar os endpoints acessando a documentação automática em:

```
http://127.0.0.1:8000/docs
```

## Dependências

Todas as dependências do projeto estão listadas no arquivo `requirements.txt`.
