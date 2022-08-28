import pandas as pd
import re

save_dir = '/Users/vistratov/dev_repos/search4duplicate_files'

# fullpath = '/Volumes/home/__PHOTOS/_Слайды (сканы)/1978 Алушта Одесса-слайды/1979-odessa_049.jpg.deadbolt'


df = pd.read_pickle('search4duplicate_files/_PHOTOS_deadbolt_file_path_list.pkl')
df.columns = ['id','full_path']
# print(df)
print('='*80)

# df.str.extract(r'([])(\.)')
# df = df.str.replace(r'debolt', '')

# df = df.full_path.str.removesuffix('.deadbolt')

df['real_path'] = df.full_path.str.replace('\/','   ')
df.real_path = df.real_path.str.removesuffix('.deadbolt')

df['ext_file'] = df.real_path.str.extract(r'\b(\w+)$', expand = True)
# df['name_file'] = 0
df['name_file'] = df.real_path.str.extract(r'\b(\w+)\.', expand = True)


df.to_csv((save_dir + "/realname_file_path_list.csv"))
print(df)
