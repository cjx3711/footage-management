# Refer to README.md for explainations
import os
import pathlib
import datetime
import time
import re

folders_checked = 0
files_moved = 0
files_skipped = 0
start_time = time.perf_counter()
folder_regex = re.compile(r'^\d{6}')

folders = [f for f in os.listdir('.') if os.path.isdir(f)]
for fo in folders:
  if re.match(folder_regex, fo):
    # print(f"Folder detected: {fo}")
    files = [f for f in os.listdir(f'./{fo}') if os.path.isfile(f'./{fo}/{f}')]
    for f in files:
      source = f'./{fo}/{f}'
      destination = f'./{f}'
      if not os.path.exists(destination):
        os.rename(source, destination)
        files_moved += 1
      else:
        print(f'File exists. Did not move {source}')
        files_skipped += 1

end_time = time.perf_counter()
print("-------------------------------")
print(f"Took {end_time - start_time:0.2f} seconds to complete")
print(f"Total files processed: {files_moved + files_skipped}")
print(f"Total files moved:     {files_moved}")
print(f"Total files skipped:   {files_skipped}")
print(f"Total folders checked: {folders_checked}")


[f for f in os.listdir(f'./{fo}')]