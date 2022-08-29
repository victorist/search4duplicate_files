import collections # for sort dictionary
import hashlib     # Default python hash operation library
import os, shutil, sys, time, random, argparse
import logging
# import six
# import imagehash
from PIL import Image

import pandas as pd
import datetime

# Define logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_file_paths (directory, extensions=None):
	"""
	Collect all files as an extension from given directory and return their paths list
	:param directory: <string> directory name
	:param extensions: <string> file extension, using for file type filter. Default value is []
	:return: <list> paths of files
	"""

	file_path_list = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			if extensions != "":

				if filename.split(".")[-1] in extensions:
					file_path = os.path.join(root, filename)
					file_path_list.append(file_path)
					logger.debug('File path : ', file_path)

			else:  # Collect all files under directory
					file_path = os.path.join(root, filename)
					file_path_list.append(file_path)

					logger.debug('File path : ', file_path)

	logger.info("Number of file found : "+str(len(file_path_list)))

	return file_path_list

    # /Users/vistratov/dev_repos/FatigueDetectionSoftwarePackage
    

# directory = '/Users/vistratov/Pictures' # директория с файлами
directory = '/Volumes/home/__PHOTOS/' # директория с файлами

save_dir = '/Users/vistratov/dev_repos/search4duplicate_files'

print('_'*80)
print('Старт формирования списка файлов: ' + str(datetime.datetime.now()))

# search files with 'deadbolt' extention
file_paths = get_file_paths (directory, extensions='*.deadbolt')


# print(file_paths)


df = pd.DataFrame(file_paths)
# print(df)

df.to_csv(save_dir + "/deadbolt_file_path_list.csv")
df.to_pickle((save_dir + "/deadbolt_file_path_list.pkl"))

print('Список файлов создан: ' + str(datetime.datetime.now()))
print('Количество найденных файлов: ' + str(len(file_paths)))
print('#'*80)
