from fastapi import FastAPI
import sys

sys.path.append("..")

#from exemplo.codigo_de_exemplo import listar_produtos
from resposta.repositorio_produtos import pesquisar_produto_por_nome, listar_produtos,\
                                            pesquisar_produtos_por_intervalo_valor,\
                                            pesquisar_produtos_por_intervalo_nota

app = FastAPI()

@app.get("/listar_produtos")
def listar_produtos_e_commerce():
    """Lista todos os produtos encontrados na página de e-commerce"""
    lista_de_produtos = listar_produtos()
    resposta = dict(produtos=lista_de_produtos)
    return resposta


@app.get("/consultar_produto/{nome_produto}")
def consultar_produto_por_nome(nome_produto: str):
    """Busca os detalhes do produto pelo nome"""
    pesquisa_de_produto = pesquisar_produto_por_nome(nome_produto.lower())
    return pesquisa_de_produto


@app.get("/consultar_produto_por_valor/{valor_min}&{valor_max}")
def consultar_por_valor(valor_min: float, valor_max: float):
    """Busca os produtos no intervalo de valores fornecidos"""
    consulta_produto_por_valor = pesquisar_produtos_por_intervalo_valor(valor_min, valor_max)
    return consulta_produto_por_valor


@app.get("/consultar_produto_por_nota/{nota_min}&{nota_max}")
def consultar_por_nota(nota_min: float, nota_max: float):
    """Busca os produtos no intervalo de notas fornecidas"""
    consulta_produto_por_nota = pesquisar_produtos_por_intervalo_nota(nota_min, nota_max)
    return consulta_produto_por_nota