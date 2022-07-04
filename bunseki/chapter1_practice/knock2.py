import pandas as pd
from pprint import pprint

# headerをつけて読み込み
data = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None, dtype=object)

'''
print(data.columns)
print(len(data.columns))
print(data)
'''

pprint(data.head())
pprint(data.dtypes)

