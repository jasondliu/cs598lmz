import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/db/user.db")
import os
import time

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.start_time = time.time()
        self.session_data = []
        self.users = []
        self.sections = []
        self.commands = []
        self.rules = []
        self.block_rules = []
        self.tuples = []
        self.num_stats = []
        self.top_websites = []

        # Setup
        self.setup_users()
        self.setup_sections()
        self.setup_commands()
        self.setup_rules()
        self.setup_block_rules()
        self.create_log_table()

    def __del__(self):
        pass

    def run(self):
        print("The Server has started")
        self.next_session()

        time.sleep(60)
        while True:
            self.next_session()

    def next_session
