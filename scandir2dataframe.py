import os
import pandas as pd
from os.path import join, getsize
import datetime


directory = '/Volumes/home/__PHOTOS' # директория с файлами
save_dir = '/Users/vistratov/dev_repos/search4duplicate_files'

print('_'*80)
print('Старт формирования списка файлов: ' + str(datetime.datetime.now()))

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

df1.to_csv(save_dir + '/qnap_photos_file_list.csv')
df1.to_pickle(save_dir + '/qnap_photos_file_list.pkl')

print('='*20)
print('Список файлов создан: ' + str(datetime.datetime.now()))
# SEARCH VALUE

# Ищем заданную директорию в столбце Dirs
# Так как в столбце списки, то преобразуем их в series и ищем значения в них
# regexbool, default True
# If True, assumes the pat is a regular expression.
# If False, treats the pat as a literal string.
dfs_dir = df1.loc[pd.Series(df1['Dirs']).str.contains('1',regex=False, case=False)]
dfs_dir.to_csv(save_dir + '/filelist_search_dir.csv')
dfs_dir.to_pickle(save_dir + '/filelist_search_dir.pkl')


# Ищем таким же способом нужные файлы
dfs_file = df1.loc[pd.Series(df1['Files']).str.contains('*.deadbolt',regex=False, case=False)]
dfs_file.to_csv(save_dir + '/filelist_search_file.csv')
dfs_file.to_pickle(save_dir + '/filelist_search_file.pkl')
print('Списки сохранены в .CSV и .PKL')

print('#'*80)