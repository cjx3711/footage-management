# Refer to README.md for explainations

import os
import time
import re

start_time = time.perf_counter()
files_renamed = 0

file_regex = re.compile(r'^G\w*\d+_\d+')

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  if re.match(file_regex, f):
    file_name, file_extension = os.path.splitext(f)
    file_name_parts = file_name.split("_")
    source = f'./{f}'
    destination = f'./{file_name_parts[0]}{file_extension}'
    os.rename(source, destination)
    files_renamed += 1

end_time = time.perf_counter()
print("-------------------------------")
print(f"Took {end_time - start_time:0.2f} seconds to complete")
print(f"Total files processed: {files_renamed}")