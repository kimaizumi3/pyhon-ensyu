import os
from glob import glob
import pandas as pd

# headerをつけて読み込み
data = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None, dtype=object)

mst = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/mst_column_name.txt'\
                    , encoding='shift-jis', sep='\t')

# columun_name_enの項目だけ抽出
columns = mst.column_name_en.values

# print(columns)

# dataのヘッダ行をcolumnsに設定
data.columns = columns

data = '/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data'
diff_data = '/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data/diff_*.csv'

print(os.listdir(data))
diff_files = glob(diff_data)

# print(diff_files)

diff_files.sort()
diff = pd.read_csv(diff_files[0], encoding='shift-jis', header=None, dtype=object)
print(len(diff))
print(diff.head(3))