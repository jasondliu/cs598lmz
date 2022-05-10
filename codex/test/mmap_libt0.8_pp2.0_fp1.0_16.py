import mmap
import pickle
from tqdm import tqdm
import gzip
import os
import shutil
import re

def func(x):
    global a
    a=1
    return int(x)

def find_id(s):
    if (s=="at"):
        id=1
        return id
    elif (s=="rt"):
        id=2
        return id
    elif (s=="for"):
        id=3
        return id
    elif (s=="to"):
        id=4
        return id
    elif (s=="via"):
        id=5
        return id
    elif (s=="of"):
        id=6
        return id
    elif (s=="the"):
        id=7
        return id
    elif (s=="a"):
        id=8
        return id
    elif (s=="and"):
        id=9
        return id
    elif (s=="with"):
        id=10

