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
        self.config = config
        self.update_pickle()
        self.current_table_name = self.get_current_table_name()
        
    def close_conn(self):
        self.conn.close()

    def get_current_table_name(self):
        self.cur.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\' AND table_name LIKE \'vdisk%%
