import pandas as pd

# csv 読み込み
data = pd.read_csv('~/study/Python/python演習/分析編/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis')

# head()で最初の五行を表示
print(data.head())
# data行を表：ｗ示
print(len(data))

# headerをつけて読み込み
data = pd.read_csv('~/study/Python/python演習/分析編/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None)

print(data.head())
print(len(data))

# aaaaaaaaaaa

