import pandas as pd
from pprint import pprint

# csv 読み込み
data = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis')

# head()で最初の五行を表示
pprint(data.head())
# data行を表：ｗ示
pprint(len(data))

# headerをつけて読み込み
data = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None)

pprint(data.head())
pprint(len(data))

