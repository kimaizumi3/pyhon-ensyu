import os
from pprint import pprint
from glob import glob
import pandas as pd

# headerをつけて読み込み
data = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None, dtype=object)

os.listdir('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data')
# list型であることを確認
# pprint(type(os.listdir('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data')))

mst = pd.read_csv('~/study/python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/mst_column_name.txt'\
                    , encoding='shift-jis', sep='\t')

# columun_name_enの項目だけ抽出
columns = mst.column_name_en.values

# pprint(columns)

# dataのヘッダ行をcolumnsに設定

# data = '/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data'
diff_data = '/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data/diff*.csv'

data.columns = columns
diff_files = glob(diff_data)
# pprint(diff_files)

diff_files.sort()
diff = pd.read_csv(diff_files[0], encoding='shift-jis', header=None, dtype=object)
pprint(len(diff))
pprint(diff.head(3))

diff.columns = columns
diff = diff.loc[diff['prefectureName'] == '静岡県']
pprint(len(diff))
pprint(diff.head(3))

# テスト用の変数にdataの中身をコピー
data_test = data 
# 既存の件数を確認
pprint(len(data_test))
# 既存の件数が正しいことを確認
pprint(len(data_test) == len(data))
# 差分の件数を確認
pprint(len(diff))
pprint(type(diff))
# テスト用の変数に差分データを追加
data_test = data_test.append(diff)
# # 追加後の件数を確認
pprint(len(data_test))
# # 追加後のデータの末尾3件を確認
pprint(data_test.tail(3))

for f in diff_files:
    diff = pd.read_csv(diff_files[0], encoding='shift-jis', header=None, dtype=object)
    diff.columns = columns
    diff = diff.loc[diff['prefectureName'] == '静岡県']
    data_test = data_test.append(diff)
    
pprint(data)
pprint(data.describe())

# 重複したデータを具体的に確認
# pprint(data[data["corporateNumber"].duplicated()])

# 重複データの削除
# data.drop_duplicates(subset='corporateNumber', keep='last', inplace=True)

# 欠損値の集計
data.isna().sum()