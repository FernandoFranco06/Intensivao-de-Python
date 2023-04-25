import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.PAUSE = 0.5

# -----Abre o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=861, y=625)
time.sleep(2)
pyautogui.hotkey("win", "up")

# -----Entra no site
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(2)

# -----Faz login
pyautogui.click(x=950, y=435)
pyautogui.write("login")
pyautogui.click(x=920, y=529)
pyautogui.write("1234")
pyautogui.click(x=933, y=616)

time.sleep(3)

# -----Exporta a base de dados
pyautogui.click(x=445, y=424)
pyautogui.click(x=1655, y=195)
pyautogui.click(x=1424, y=672)

time.sleep(10)

# -----Lê a tabela e calcula os indicadores
tabela = pd.read_csv(r"C:\Users\ferna\Downloads\Compras.csv", sep=";")

total_gasto = tabela["ValorFinal"].sum()    # Soma os valores
quantidade = tabela["Quantidade"].sum()     # Soma a quantidade
preco_medio = total_gasto / quantidade      # Calcula o preço médio

# -----Abre o Gmail e envia um e-mail com os indicadores
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=113, y=209)
# Remetente
pyautogui.write("fernandorfranco06@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# Assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Corpo do e-mail
texto = f"""                                    
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,} 
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Fernando Franco
"""
pyperclip.copy(texto)

# Envia o e-mail
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
