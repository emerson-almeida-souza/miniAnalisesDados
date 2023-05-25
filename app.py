import pandas as pd

#Como aumentar as vendas ?
tabela = pd.read_excel('vendas.xlsx')
print(tabela)

faturamentoTotal = tabela['Valor Final'].sum()
print(faturamentoTotal)
# #Análise top-down
faturamentoPorLoja = tabela[['Valor Final', 'ID Loja']].groupby('ID Loja').sum('Valor Final')

#Detalhe
faturamentoPorProduto = tabela[['Valor Final', 'Produto' ,'ID Loja']].groupby(['ID Loja', 'Produto']).sum('Valor Final')
print(faturamentoPorProduto)

#Resultado: Vender mais bermudas lisas igual o iguatemi Campinas