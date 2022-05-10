from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:24:40 2017

@author: zhcao
"""

import sys
import os
import re
import shutil

def get_file_list(dir_name, file_list):
    newDir = dir_name
    if os.path.isfile(dir_name):
        file_list.append(dir_name)
    elif os.path.isdir(dir_name):
        for s in os.listdir(dir_name):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir_name,s)
            get_file_list(newDir, file_list)  
    return file_list

def get_file_content(file_name):
    with open(file_
