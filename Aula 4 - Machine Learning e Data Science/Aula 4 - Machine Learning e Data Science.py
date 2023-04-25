# OBJETIVO: Prever o preço de um barco baseado em suas características (ano, material, etc)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# -----Extração/Obtenção de Dados
tabela = pd.read_csv("barcos_ref.csv")
print(tabela)

# -----Ajuste de Dados (Tratamento/Limpeza)
print(tabela.info())

# -----Análise Exploratória
# Encontrar correlação entre as características
correlacao = tabela.corr()[["Preco"]]
print(correlacao)

sns.heatmap(correlacao, cmap="Blues", annot=True)    # Cria gráfico
plt.show()                                           # Exibe gráficos

# -----Modelagem + Algoritmos (Inteligência Artificial)
# Dividir a base em x e y
x = tabela.drop("Preco", axis=1)
y = tabela["Preco"]

# train test split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2)

# Criar a inteligência artificial - Regreessão linear e random forest
modelo_regressaoLinear = LinearRegression()
modelo_randomForest = RandomForestRegressor()

# Treinar a inteligência artificial
modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_randomForest.fit(x_treino, y_treino)

# -----Interpretação de Resultados
# Escolher o melhor modelo -> R²
previsao_regressaoLinear = modelo_regressaoLinear.predict(x_teste)
previsao_randomForest = modelo_randomForest.predict(x_teste)

print(r2_score(y_teste, previsao_regressaoLinear))
print(r2_score(y_teste, previsao_randomForest))

# Visualizar as previsões
tabela_auxiliar = pd.DataFrame()    # Tabela vazia
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["RandomForest"] = previsao_randomForest
tabela_auxiliar["RegressaoLinear"] = previsao_regressaoLinear

sns.lineplot(data=tabela_auxiliar)
plt.show()

# Fazer novas previsões
tabela_nova = pd.read_csv("novos_barcos.csv")
print(tabela_nova)

previsao = modelo_randomForest.predict(tabela_nova)
print(previsao)
