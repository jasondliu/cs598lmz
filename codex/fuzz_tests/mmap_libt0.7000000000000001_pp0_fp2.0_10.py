import mmap
import argparse
import sys
import os

parser = argparse.ArgumentParser(description = "List all the .dat files in the directory. Split the .dat files into multiple .dat files by their sizes. The default value for the size of each .dat file is 1GB.")
parser.add_argument("-s", "--size", help = "The size for each .dat file in GB. The default value is 1GB.", type = int, default = 1)
args = parser.parse_args()

def split_file(filename, size):
    """Split the file into smaller ones by a given size. The size is measured in GB. The default size is 1GB"""
    
    # If the file size is less than the given size, copy the file to another file
    if os.path.getsize(filename) < size * 1024 * 1024 * 1024:
        tmp = open(filename + ".tmp", "w")
        tmp.write(open(filename, "r").read())
        tmp.close()
        os.remove(filename)
        os.rename(filename + ".tmp", filename)
       
