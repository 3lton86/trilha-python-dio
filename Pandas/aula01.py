import pandas as pd
import matplotlib as mp

zposcst101 = '/Users/eltonfernandes/Documents/dados/df_101.csv'
df = pd.read_csv(zposcst101)
df = pd.read_csv(zposcst101, delimiter=';', encoding='utf-8')

print(df.head(n=5))
print(df.info)
print(df.shape)
print(df.isnull().sum())
print(df.describe())



