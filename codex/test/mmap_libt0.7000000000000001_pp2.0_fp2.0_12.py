import mmap
import os
import pickle
import random
import sys
import time
import zipfile

#----------------------------------------------------------------------------

class Cache:
    def __init__(self, dir_name, max_items = 1000000):
        self.dir_name = dir_name
        self.max_items = max_items
        self.dir_path = os.path.join(dir_name, 'cache')
        self.lock_path = os.path.join(dir_name, 'cache.lock')
        self.size = 0
        if os.path.isdir(self.dir_path):
            self._lock()
            self._load_cache()
        else:
            self._create_cache()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._commit_cache()
        self._unlock()

    def _lock(self):
        if os.path.isfile(self.lock_path):
            raise Exception('Cache directory is locked: ' + self.dir_name)
