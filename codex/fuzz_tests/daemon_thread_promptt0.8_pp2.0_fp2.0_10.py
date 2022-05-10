import threading
# Test threading daemon
import time
# Test threading sleep

import sys
# test cmd input



class Data_center():
    def __init__(self):
        self.init_env()
        self.init_flag()
        self.init_socket()
        self.init_thread()
        self.init_timer()
        self.init_cmd()

    '''init'''
    def init_env(self):
        '''init env params'''

    def init_flag(self):
        self.flag_run = True
        self.flag_con = False
        self.flag_done = False
        self.flag_msg_recv_over = False
        self.flag_chat = False

    def init_socket(self):
        #socket
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init_thread(self):
        self.thd_id = []

    def init_timer(self):
        self.timer_id = []

    def init_cmd(self):
        self
