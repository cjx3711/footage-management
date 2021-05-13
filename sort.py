# Refer to README.md for explainations
import os
import pathlib
import datetime

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  if f != 'sort.py':
    fname = pathlib.Path(f)
    mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
    folder = mtime.strftime("%y%m%d")
    source = f'./{f}'
    destination = f'./{folder}/{f}'
    print(f'File detected: {f} created: {mtime}')
    if not os.path.exists(folder):
      print(f'Making folder: {folder}')
      os.makedirs(folder)
    if not os.path.exists(destination):
      os.rename(source, destination)
      print(f'Moved to {destination}')
    else:
      print(f'File exists. Did not move {source}')