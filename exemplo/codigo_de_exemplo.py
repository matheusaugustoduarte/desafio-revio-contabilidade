import bs4

def listar_produtos() -> list:
    """Método de exemplo para interção com o html da página do e-commerce"""

    # Carrega o arquivo html
    html_pagina = open("page/revio-e-commerce.html")

    #Parsea o arquivo
    soup = bs4.BeautifulSoup(html_pagina, "html.parser")

    #Captura o grid html com todos os produtos
    grid_de_produtos = soup.find("div", class_="products-grid")

    #Cria uma lista apenas com html específico dos produtos
    produtos = grid_de_produtos.find_all("div", attrs={"class":"product-card"})

    #Cria uma lista apenas com o atributo do nome dos produtos
    nomes_de_produtos = [produto.find("h3").text for produto in produtos]

    return nomes_de_produtos


if __name__ == "__main__":
    resultado = listar_produtos()
    print(resultado)