import pandas as pd

# headerをつけて読み込み
data = pd.read_csv('~/study/Python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/22_shizuoka_all_20210331.csv'\
                    , encoding='shift-jis', header=None, dtype=object)

mst = pd.read_csv('~/study/Python/python演習/bunseki/'\
                    '100knock-process-visualization/chapter-1/data/mst_column_name.txt'\
                    , encoding='shift-jis', sep='\t')

# columun_name_enの項目だけ抽出
columns = mst.column_name_en.values

# dataのヘッダ行をcolumnsに設定
data.columns = columns