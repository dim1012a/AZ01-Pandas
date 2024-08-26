import pandas as pd

df_guit = pd.read_csv('GuitarModels.csv')

print(df_guit.head())
print(df_guit.info())
print()
print(df_guit.describe())
print()

print('---------------------------------------------')
print('Средняя з/п по городам:')
df_dz = pd.read_csv('dz.csv')

print(df_dz.groupby('City')['Salary'].mean())

