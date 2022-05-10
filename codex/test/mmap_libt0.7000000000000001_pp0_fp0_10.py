import mmap
import time
import os
import re
import sys

class LogHandler:
    def __init__(self, filename):
        self.filename = filename

    def tail(self):
        f = open(self.filename, 'r')
        location = 0

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                f.seek(location)
            else:
                location = f.tell()
                yield line


def get_table_name(filename):
    table_name = ''
    if filename.find('_') < 0:
        return table_name
    else:
        table_name = filename.split('_')[1].split('.')[0]
        return table_name

