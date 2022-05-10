import mmap
import os
import sys
import time

from . import config
from . import utils

class Cache:
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        self.cache_path = os.path.join(self.cache_dir, "cache")
        self.cache_map = None
        self.cache_fd = None
        self.cache_size = 0
        self.cache_next_offset = 0
        self.cache_next_offset_lock = threading.Lock()
        self.cache_lock = threading.Lock()
        self.cache_mmap_lock = threading.Lock()
        self.cache_mmap_count = 0
        self.cache_mmap_count_lock = threading.Lock()
        self.cache_mmap_count_cond = threading.Condition(self.cache_mmap_count_lock)

    def open(self):
        self.cache_fd = os.open(self.cache_path, os.O_RDWR | os.O_CREAT)
