import mmap
import time

# import mecab_helper

from config import *


class Mecab:

    def __init__(self):
        self.mecab_helper = MecabHelper()
        self.dict_size = 0
        self.dict_file = None
        self.dict_mmap = None

    def open_dict(self, dict_filename):
        self.dict_file = codecs.open(dict_filename, 'r', 'utf-8')
        self.dict_size = os.path.getsize(dict_filename)
        self.dict_mmap = mmap.mmap(self.dict_file.fileno(), self.dict_size,
                                   access=mmap.ACCESS_READ)

    def close_dict(self):
        self.dict_mmap.close()
        self.dict_file.close()

    def split(self, text):
        words = []

        if not self.dict_mmap:
            self.open_dict(MECAB_DIC_PATH)

        start =
