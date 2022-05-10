import mmap
import os
import sys
from datetime import datetime
from os.path import exists, join, getsize
from shutil import copyfile

from utils.logger import get_logger

logger = get_logger(__name__)


class FileHandler:
    def __init__(self, file_path, file_name, file_extension):
        self.file_path = file_path
        self.file_name = file_name
        self.file_extension = file_extension
        self.full_file_path = join(self.file_path, self.file_name + self.file_extension)

    def file_exists(self):
        return exists(self.full_file_path)

    def file_size(self):
        return getsize(self.full_file_path)

    def create_directory(self):
        if not exists(self.file_path):
            os.makedirs(self.file_path)

    def create_file(self, file_content=None):
        if self.file
