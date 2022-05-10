import ctypes
import ctypes.util
import threading
import sqlite3
from urllib.parse import urlparse
from . import __version__, __description__
from .utils import Bcolors, MappedList, get_host
from .pcap import Pcap


class Sqlite:
    def __init__(self, log_path, log_name=None, log_dir=None, log_db=None):
        self.log_path = log_path
        self.log_name = log_name
        self.log_dir = log_dir
        self.log_db = log_db
        self.db_hosts = MappedList()
        self.db_hosts_list = []
        self.db_hosts_dict = {}
        self.db_data = []
        self.db_urls = MappedList()
        self.db_urls_list = []
        self.db_urls_dict = {}
        self.db_urls_dict_counted = {}
        self.db_domains = MappedList()
        self.db_domains_list = []
        self.db
