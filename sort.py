# Refer to README.md for explainations
import os
import pathlib
import datetime
import time

folders_created = 0
files_moved = 0
files_skipped = 0
start_time = time.perf_counter()
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  file_name, file_extension = os.path.splitext(f)
  if f != '.gitignore' and file_extension.lower() != '.py' and file_extension.lower() != '.md':
    fname = pathlib.Path(f)
    mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
    folder = mtime.strftime("%y%m%d")
    source = f'./{f}'
    destination = f'./{folder}/{f}'
    # print(f'File detected: {f} created: {mtime}')
    if not os.path.exists(folder):
      print(f'Making folder: {folder}')
      os.makedirs(folder)
      folders_created += 1
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
print(f"Total folders created: {folders_created}")