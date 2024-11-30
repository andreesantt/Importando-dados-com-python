import pandas as pd

# 1 - Importando dados

data = pd.read_excel('Importando-dados-com-python\data\VendaCarros.xlsx')
nome = 'Rodrigo'
# print(type(data))

# 2 - Selecionando Colunas específicas do dataframe
df = data[['Fabricante', 'ValorVenda', 'Ano']]
print(df)

# 3 - Criar tabela pivô
pivot_table = df.pivot_table(
    index='Ano',
    columns='Fabricante',
    values='ValorVenda',
    aggfunc='sum'
)
print(pivot_table)

# 4 - Exportar tabela pivô em arquivo excel
pivot_table.to_excel('Importando-dados-com-python/pivot_table.xlsx', 'Relatório')