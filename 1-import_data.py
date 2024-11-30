import pandas as pd
# 1 - Importando dados
data = pd.read_excel('Importando-dados-com-python\data\VendaCarros.xlsx')
print(data)
# 2 - Lista os primeiros registros
print(data.head())
# 3 - Lista os últimos registros
print(data.tail())
# 4 - contagem de valores por Fabricante
print(data['Fabricante'].value_counts())