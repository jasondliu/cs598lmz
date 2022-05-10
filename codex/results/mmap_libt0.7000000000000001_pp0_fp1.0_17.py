import mmap
import numpy as np
import os
import re
import shutil
import struct
import sys

from math import pi, sin
from PIL import Image

def ls(path):
    return os.listdir(path)

def cd(path):
    return os.chdir(path)

def cp(src, dst):
    return shutil.copyfile(src, dst)

def rm(path):
    return os.remove(path)

def rmdir(path):
    return shutil.rmtree(path)

def mkdir(path):
    return os.makedirs(path)

def mv(src, dst):
    return shutil.move(src, dst)

def exists(path):
    return os.path.exists(path)

def isfile(path):
    return os.path.isfile(path)

def isdir(path):
    return os.path.isdir(path)

def join(*args):
    return os.path.join(*args)

def pwd():
   
