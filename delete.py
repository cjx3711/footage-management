# Refer to README.md for explainations

import os
import time
import re


folders_checked = 0
files_deleted = 0
start_time = time.perf_counter()
folder_regex = re.compile(r'^\d{6}')


def process_file(source_folder, file):
  global files_deleted
  file_name, file_extension = os.path.splitext(file)
  if file_extension.lower() == '.thm' or file_extension.lower() == '.lrv':
    source = f'{source_folder}/{file}'
    destination = f'deleted/{file}'
    os.rename(source, destination)
    files_deleted += 1


# Ensure deleted folder exists
if not os.path.exists('deleted'):
  os.makedirs('deleted')

# Process top level files
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  process_file('.', f)

# Process folders
folders = [f for f in os.listdir('.') if os.path.isdir(f)]
for fo in folders:
  if re.match(folder_regex, fo):
    folders_checked += 1
    files = [f for f in os.listdir(f'./{fo}') if os.path.isfile(f'./{fo}/{f}')]
    for f in files:
      process_file(fo, f)


end_time = time.perf_counter()
print("-------------------------------")
print(f"Took {end_time - start_time:0.2f} seconds to complete")
print(f"Total files deleted:     {files_deleted}")
print(f"Total folders checked:   {folders_checked}")
