import pandas as pd
import matplotlib as mp

devol101 = '/Users/eltonfernandes/Documents/dados/Devolucao_vendas_VD/devol101.csv'
devol102 = '/Users/eltonfernandes/Documents/dados/Devolucao_Vendas_VD/devol102.csv'
# df_101 = pd.read_csv(devol101)
df_101 = pd.read_csv(devol101, delimiter=';', encoding='utf-8')
df_102 = pd.read_csv(devol102)
df_102 = pd.read_csv(devol102, delimiter=';', encoding='utf-8') 

# print(df_101.head(n=5))
# print(df_102.head(n=5))
# print(df_101.describe())

df = pd.merge(df_101, df_102, on="Chave de Acesso à NFe", how='inner')

print(df.head(n=10))
print(df.shape)
# print(df_101.shape)
# print(df_102.shape)