import pandas as pd

# headerをつけて読み込み
data = pd.read_csv('~/study/Python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None, dtype=object)

'''
print(data.columns)
print(len(data.columns))
print(data)
'''

print(data.head())
print(data.dtypes)

