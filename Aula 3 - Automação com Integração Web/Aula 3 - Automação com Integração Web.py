from selenium import webdriver
import pandas as pd
import unicodedata

# -----Abrir o navegador
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")    # get -> Entra no site especificado

# -----Importar a base de dados
tabela = pd.read_excel("commodities.xlsx")
print(tabela)

# -----Pesquisar os preços e atualizá-los na tabela
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]

    # Formatar o nome do produto
    produto = unicodedata.normalize("NFKD", produto).encode("ascii", "ignore")

    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')      # Pega o preço no site
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = preco

# -----Decidir quais produtos comprar e exportar a base de dados
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]

# -----Exportar a base para o excel e fechar o navegador
tabela.to_excel("commodities_atualizado.xlsx", index=False)
navegador.quit()
