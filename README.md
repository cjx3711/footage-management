# Footage Management

## Overview
I spend a lot of time trying to sort and manage my footage from my gopros and cameras. This is a repository to store all the python scripts that I need to organise my photos for me.

## Running
This is coded in python 3. To run it, simply go into the terminal and type `python3 file.py`
I have tested this on windows using the linux subsystem. I do not know if it works on other OSes

## Scripts

`sort.py`
This takes all the files in a directory and puts them into subdirectories based on the creation date.
The folder will be named according to the date format YYMMDD
It will create folders if required.
It will not move a file if it already exists
This is a destructive operation and will move the files.

For example:
```
Original
  File     Created
  001.mp4  20 Mar 2020
  002.mp4  20 Mar 2020
  003.jpg  21 Mar 2020
  004.mp4  21 Mar 2020

After script
  200320/
    001.mp4
    002.mp4
  200321/
    003.jpg
    004.mp4
```

`merge.py`
This takes all the files in subdirectories and moves them to the main directory. It is not recursive and only works on directories one level deep. It will not delete the folders.
This is a destructive operation and will move the files.

For example:
```
Original
  200320/
    001.mp4
    002.mp4
  200321/
    003.jpg
    004.mp4

After script
  /
    200321/
    200320/
    001.mp4
    002.mp4
    003.jpg
    004.mp4
```



`rename.py`
This is specific to a workflow for GoPro cameras. The file exported by an app will be named something like `GX010733_1610964461492.MP4` while the same file from the camera is simply named `GX010733.MP4`. This goes through all the files in a directory and removes the bit after the `_`

```
Original
  GX010733_1610964461492.MP4

After script
  GX010733.MP4
```