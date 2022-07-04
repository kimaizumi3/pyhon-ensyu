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
                    '100knock-process-visualization/chapter-1/data/mst_column_name.txt',\
                    encoding='shift-jis', sep='\t')

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

pprint('------kcnock7-------')

mst_process_kbn = pd.read_csv('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_process_kbn.csv' , dtype=object)


# 追加（processがint64だったため変換）
# mst_process_kbn['process'] = mst_process_kbn['process'].astype(object)

pprint(mst_process_kbn)

# pprint(data.dtypes)
# print("------------------")
# pprint(mst_process_kbn.dtypes)

# processをマージ
data = data.merge(mst_process_kbn, on='process', how='left')
pprint(len(data.columns))
pprint(data.head(3))

# mst_correct_kbnをマージ
mst_correct_kbn = pd.read_csv('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_correct_kbn.csv', encoding='shift-jis', dtype=object)

pprint(mst_correct_kbn)

data = data.merge(mst_correct_kbn, on='correct', how='left')
pprint(len(data.columns))
pprint(data.head(3))

# mst_corp_kindをマージ
mst_corp_kind = pd.read_csv('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_corp_kind.csv', dtype=object)

pprint(mst_corp_kind)

data = data.merge(mst_corp_kind, on='kind', how='left')
pprint(len(data.columns))
pprint(data.head(3))

# mst_latestをマージ
mst_latest = pd.read_csv('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_latest.csv', dtype=object)

pprint(mst_latest)

data = data.merge(mst_latest, on='latest', how='left')
pprint(len(data.columns))
pprint(data.head(3))

# mst_hihyojiをマージ
mst_hihyoji = pd.read_csv('/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_hihyoji.csv', dtype=object)

pprint(mst_hihyoji)

data = data.merge(mst_hihyoji, on='hihyoji', how='left')
pprint(len(data.columns))
pprint(data.head(3))


