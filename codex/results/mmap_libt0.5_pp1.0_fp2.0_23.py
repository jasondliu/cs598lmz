import mmap
import sys
import os
import re
import random

class File_Read:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file_size = os.path.getsize(self.file_name)
        self.file_read = open(self.file_name,"rb")
        self.file_mmap = mmap.mmap(self.file_read.fileno(),self.file_size,access=mmap.ACCESS_READ)

    def __del__(self):
        self.file_mmap.close()
        self.file_read.close()

    def read_file_line(self):
        file_lines = self.file_mmap.readlines()
        return file_lines


class File_Write:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file_write = open(self.file_name,"wb")

    def __del__(self):
        self.file_write.close()

   
