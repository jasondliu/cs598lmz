import mmap
# Test mmap.mmap(0, 5*1024*1024*1024, 'foo', mmap.ACCESS_READ)
"""
"""

# from gevent import monkey
# monkey.patch_all()

from multiprocessing import Process, Queue
import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pfio.filemap import Filemap
from pfio.baseio import get_io_path, get_io_host, get_io_port, default_cache_size, default_io_size, default_partition_count, default_chunk_size, default_ip, default_port
from pfio.helper import policy_time, check_configuration
from pfio.client import *
from pfio.keychain import *
from pfio.metadata import FileMeta, ObjectMeta
from pfio.utils import create_container_if_not_exists, create_cache_policy, get_value_from_config_
