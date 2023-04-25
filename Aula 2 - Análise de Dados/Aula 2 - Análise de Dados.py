import pandas as pd
import plotly.express as px

# -----Importar a base de dados
tabela = pd.read_csv("clientes.csv", sep=";", encoding="latin")

# -----Visualizar a base de dados (entender informações e procurar erros)
print("TABELA: ")
print(tabela)
print("-" * 60)
print("INFO:")
print(tabela.info())

# -----Tratamento de dados
tabela = tabela.drop("Unnamed: 8", axis=1)    # Deletar coluna inútil
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")    # Arrumar o tipo errado das informações
tabela = tabela.dropna()    # Corrigir informações vazias

# -----Análise inicial -> Entender as notas dos clientes
print("-" * 60)
print("DESCRIBE:")
print(tabela.describe())    # Ver indicadores, em especial a média das notas

# -----Análise completa -> Entender como cada característica impacta na nota
# Cria e exibe os gráficos para cada coluna
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=5)
    grafico.show()

# -----Conclusões tiradas a partir dos gráficos
# Perfil ideal de cliente:
# Acima de 15 anos (não tem muita diferença entre as faixas etárias a partir disso)
# Faixa salarial não parece fazer tanta diferença
# Áreas de trabalho: Entretenimento e Artista (evitar Construção)
# Experiência entre 10 e 15 anos
# Famílias não tão grandes (no máximo 7 pessoas)
