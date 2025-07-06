import pandas as pd

print("Iniciando o script de processamento de dados...")

dados = {'Produto': ['Notebook', 'Mouse', 'Teclado'], 'Preco': [5000, 150, 200]}
df = pd.DataFrame(dados)

print("\nDataFrame criado:")
print(df)

print("\nProcessamento concluído com sucesso!")