import mmap
import multiprocessing
import os
import re
import subprocess
import sys
import time

from pymongo import MongoClient

from config import Config
from log import log

class FileProcessor(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_type = None
        self.file_size = None
        self.file_sha1 = None

    def get_file_type(self):
        try:
            file_type = subprocess.check_output(['file', '-b', self.file_name])
        except subprocess.CalledProcessError:
            log.error('Could not get file type for file %s' % self.file_name)
            return None

        # Strip out the file name from the file command output
        self.file_type = file_type.split(':')[0]

