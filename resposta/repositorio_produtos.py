from bs4 import BeautifulSoup


def buscar_produtos_no_html():
    # Abre o arquivo HTML e após o uso ele fecha
    with open("page/revio-e-commerce.html", encoding="utf-8") as html_pagina:
        # Parsea o arquivo (transforma o HTML em algo que o Python consegue entender e mexer com facilidade)
        soup = BeautifulSoup(html_pagina, "html.parser")

    # Captura o grid html com todos os produtos
    grid_de_produtos = soup.find("div", class_="products-grid")

    # Cria uma lista apenas com html específico dos produtos
    produtos_html = grid_de_produtos.find_all(
        "div", attrs={"class": "product-card"})

    return produtos_html


def listar_produtos() -> list:
    # Chama a função para buscar os dados dos produtos.
    produtos_html = buscar_produtos_no_html()
    # Cria uma lista apenas com o atributo do nome dos produtos
    nomes_de_produtos = [produto.find("h3").text for produto in produtos_html]

    return nomes_de_produtos


def pesquisar_produto_por_nome(nome_buscado: str) -> list:
    # Chama a função para buscar os dados dos produtos.
    produtos_html = buscar_produtos_no_html()

    # Lista dos produtos apenas com os atributos (nome, nota e valor)
    produtos = []

    for p in produtos_html:
        nome = p.find("h3").text
        nota = float(p.find("span", class_="rating-value").text.strip())
        texto_valor = p.find("span", class_="current-price").text.strip()
        valor = float(
            texto_valor
            .replace("R$", "")  # tira o símbolo
            .replace(".", "")  # tira separador de milhar
            .replace(",", ".")  # ajusta o decimal
        )
        produtos.append({"nome": nome, "nota": nota, "valor": valor})

    # Filtra os produtos que contêm o nome buscado (ignorando maiúsculas/minúsculas) - Modo list comprehension
    resultados = [
        produto for produto in produtos
        if nome_buscado in produto["nome"].lower()
    ]

    if resultados:
        return resultados
    else:
        return {"mensagem": "Produto não encontrado"}


def pesquisar_produtos_por_intervalo_valor(valor_min: float, valor_max: float) -> list:
    # Chama a função para buscar os dados dos produtos.
    produtos_html = buscar_produtos_no_html()

    # Lista dos produtos apenas com os atributos (nome, nota e valor)
    produtos = []

    for p in produtos_html:
        nome = p.find("h3").text
        nota = float(p.find("span", class_="rating-value").text.strip())
        texto_valor = p.find("span", class_="current-price").text.strip()
        valor = float(
            texto_valor
            .replace("R$", "")
            .replace(".", "")
            .replace(",", ".")
        )
        if valor_min <= valor <= valor_max:
            produtos.append({"nome": nome, "nota": nota, "valor": valor})

    if produtos:
        return produtos
    else:
        return {"mensagem": "Nenhum produto encontrado no intervalo informado"}


def pesquisar_produtos_por_intervalo_nota(nota_min: float, nota_max: float) -> list:
    # Chama a função para buscar os dados dos produtos.
    produtos_html = buscar_produtos_no_html()

    # Lista dos produtos apenas com os atributos (nome, nota e valor)
    produtos = []

    for p in produtos_html:
        nome = p.find("h3").text
        nota = float(p.find("span", class_="rating-value").text.strip())
        texto_valor = p.find("span", class_="current-price").text.strip()
        valor = float(
            texto_valor
            .replace("R$", "")
            .replace(".", "")
            .replace(",", ".")
        )
        if nota_min <= nota <= nota_max:
            produtos.append({"nome": nome, "nota": nota, "valor": valor})

    if produtos:
        return produtos
    else:
        return {"mensagem": "Nenhum produto encontrado no intervalo informado"}


if __name__ == "__main__":
    resultado1 = pesquisar_produto_por_nome()
    resultado2 = listar_produtos()
    resultado3 = pesquisar_produtos_por_intervalo_valor()
    resultado4 = pesquisar_produtos_por_intervalo_nota()
    resultado5 = buscar_produtos_no_html()
    print(resultado1)
    print(resultado2)
    print(resultado3)
    print(resultado4)
    print(resultado5)
