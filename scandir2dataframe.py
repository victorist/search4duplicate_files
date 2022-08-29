import os
import pandas as pd
from os.path import join, getsize
import datetime


# directory = '/Volumes/home/__PHOTOS' # директория с файлами
# directory = '/Volumes/home/__VIDEOS' # директория с файлами
directory = '/Volumes/home/__VIDEOS' # директория с файлами

save_dir = 'search4duplicate_files/results'

print('#'*80)
print(f"Старт формирования списка файлов: {datetime.datetime.now():%Y%m%d-%H%M-%S_%f}")

# FIRST VARIANT
# FutureWarning: 
# The frame.append method is deprecated and will be removed from pandas in a future version. 
# Use pandas.concat instead.
'''
df = pd.DataFrame( columns=['Root','Dirs','Files'])

tree = os.walk(directory)
for r, d, f in tree:
   dict = {'Root': r, 'Dirs': d, 'Files': f}
   df = df.append(dict, ignore_index = True)

print('_'*80)
# print(df)
df.to_csv(save_dir + '/filelist.csv')
print('='*80)
'''

# SECOND VARIANT ==========================================

data = []
tree = os.walk(directory)
for r, d, f in tree:
    data.append([ r, d, f ])
    # print('Директория:', r)
    # print('Путь: ', d)
    # print('файлы: ')
df1 = pd.DataFrame(data, columns=['Root', 'Dirs', 'Files'])

df1.to_csv(save_dir + '/qnap_videos_file_list'+f'{datetime.datetime.now():%Y%m%d-%H%M-%S_%f}'+'.csv')
df1.to_pickle(save_dir + '/qnap_videos_file_list'+f'{datetime.datetime.now():%Y%m%d-%H%M-%S_%f}'+'.pkl')

print('='*20)
print(f"Список файлов сформирован и сохранён: {datetime.datetime.now():%Y%m%d-%H%M-%S_%f}")
print('Списки сохранены в .CSV и .PKL')

print('='*80)