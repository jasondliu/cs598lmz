from types import FunctionType
list(FunctionType(lambda x: x, globals()).__globals__.keys())

# %%
from os import listdir
from os.path import isfile, join
mypath = "/home/jovyan/notebooks/data/raw/images/train/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# %%
from os import listdir
from os.path import isfile, join, isdir

def list_files_recursively(path):
    files = []
    for f in listdir(path):
        file = join(path, f)
        if isfile(file):
            files.append(file)
        elif isdir(file):
            files.extend(list_files_recursively(file))
    return files

mypath = "/home/jovyan/notebooks/data/raw/images/train/"
onlyfiles = list_files_recursively(mypath)

# %%
import os
import sys

def get_immediate_subdirectories(a_
