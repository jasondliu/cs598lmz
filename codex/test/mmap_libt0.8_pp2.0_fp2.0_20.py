import mmap
import sys
import time
import pickle
import psycopg2

class DB:
    def __init__(self, config):
        self.conn = psycopg2.connect(
            database = config.database,
            user = config.user,
            password = config.password,
            host = config.host,
            port = config.port)
        self.cur = self.conn.cursor()
        self.format = config.format
        self.file_lock = threading.Lock()
        self.pickle_lock = threading.Lock()
        self.pickle_name = config.pickle_name
