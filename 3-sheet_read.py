from openpyxl import load_workbook

# 1 - Lê pasta de trabalho e planilha
wb = load_workbook('Importando-dados-com-python\pivot_table.xlsx')
sheet = wb['Relatório']

# 2 - Acessando valor específico
print(sheet['A3'].value)
print(sheet['B3'].value)

# 3 - Iterando valores por meio de loop
for i in range(2, 6):
    ano = sheet['A%s' %i].value
    am = sheet['B%s' %i].value
    bt = sheet['C%s' %i].value
    print('{0} o Aston Martin vendeu {1} e o Bentley {2}'.format(ano, am, bt))