import pandas as pd


df1 = pd.read_pickle('search4duplicate_files/filelist_search_file.pkl')
# SEARCH VALUE
# Ищем заданную директорию в столбце Dirs
# Так как в столбце списки, то преобразуем их в series и ищем значения в них
# regexbool, default True
# If True, assumes the pat is a regular expression.
# If False, treats the pat as a literal string.
'''
dfs_dir = df1.loc[pd.Series(df1['Dirs']).str.contains('1',regex=False, case=False)]
dfs_dir.to_csv(save_dir + '/filelist_search_dir.csv')
dfs_dir.to_pickle(save_dir + '/filelist_search_dir.pkl')
'''

# Ищем таким же способом нужные файлы
dfs_file = df1.loc[pd.Series(df1['Files']).str.contains('.deadbolt',regex=False, case=False)]
dfs_file.to_csv(save_dir + '/filelist_search_file.csv')
dfs_file.to_pickle(save_dir + '/filelist_search_file.pkl')