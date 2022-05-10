from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in func_list)

#%%
import os
from os import path
import glob
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt");
        
        # # let's make a backup copy by appending "bak" to the name
        #dst = src + ".bak"
        # # now use the shell to make a copy of the file
        #shutil.copy(src,dst)
        # # copy over the permissions, modification times, and other info
        #shutil.copystat(src, dst)
        
        # rename the original file
        #os.rename("textfile.txt", "
