import pandas as pd
data = {'Product': ['Футболка', 'Джинсы', 'Кроссовки'],
        'Цвет': ['Красный', 'Синий', 'Черный'],
        'Размер': ['S', 'M', 'L'],
        'Цена': [1000, 2000, 3000]}

df = pd.DataFrame(data)
print(df)

df.to_csv(r'C:\Users\1\PycharmProjects\pythonProject20\test.csv')

df_import = pd.read_csv(r'C:\Users\1\PycharmProjects\pythonProject20\test.csv')

print(df_import.head())