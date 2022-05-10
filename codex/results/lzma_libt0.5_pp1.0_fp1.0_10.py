import lzma
lzma.open

import os

def get_files_in_dir(dir):
    return [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

def get_all_files_in_dir(dir):
    all_files = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            all_files.append(os.path.join(root, f))
    return all_files

def get_all_dirs_in_dir(dir):
    all_dirs = []
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            all_dirs.append(os.path.join(root, d))
    return all_dirs

def get_all_files_in_dir_with_extension(dir, extension):
    all_files = []
    for root, dirs, files in os.walk(dir):
        for f
