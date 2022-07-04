import os
from pprint import pprint
import pandas as pd

data_directory = '/home/kimaizumi/study/python/python演習/bunseki/100knock-process-visualization/chapter-1/data'
pprint(os.listdir(data_directory))

mst_process_kbn = pd.read_csv('/home/kimaizumi/study/python/'\
                              'python演習/bunseki/100knock-process-visualization/'\
                              'chapter-1/data/mst_process_kbn.csv' , dtype=object)

pprint(mst_process_kbn)
