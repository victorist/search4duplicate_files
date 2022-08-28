import pandas as pd

save_dir = '/Users/vistratov/dev_repos/search4duplicate_files'

df = pd.read_csv('search4duplicate_files/_PHOTOS_file_path_list.csv')
df.to_pickle(save_dir + '/_PHOTOS_file_path_list.pkl')