import _struct
import time
import threading
import random

import write_to_buffer
import search_all_directions
import instance
import simulation
import communication

class PathFinder():
    def __init__(self, bot, target):
        #print("Creating a PathFinder instance...")
        self.bot = bot
        self.target = target
        self.path_history = []
        self.next_pos = None
        self.found_exit = False
        self.last_path = None
        self.last_path_update = 0
        self.last_path_origin = None
        self.path_updater_instance = None
        self.path_updater_lock = threading.Lock()
        self.path_lock = threading.Lock()
        self.path_finding_instance = None
        self.path_finding_lock = threading.Lock()
        self.path_finder_thread = threading.Thread(target=self.path_finder_thread_func)
        self.path_finder_thread.start()
        self.path_up
