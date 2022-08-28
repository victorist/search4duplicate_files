# во втором варианте используется библиотека os
import os

directory = '/Volumes/home/__PHOTOS/' # директория с файлами
save_dir = '/Users/vistratov/dev_repos/search4duplicate_files'



print('_'*80)
print('Старт формирования списка файлов: ' + str(datetime.datetime.now()))

file_list = os.listdir(directory) # директория с файлами

df = pd.DataFrame(file_list)
# print(df)

df.to_csv(save_dir + "/deadbolt_file_list.csv")
df.to_pickle((save_dir + "/deadbolt_file_list.pkl"))

print('Список файлов создан: ' + str(datetime.datetime.now()))
print('Количество найденных файлов: ' + str(len(file_list)))
print('#'*80)