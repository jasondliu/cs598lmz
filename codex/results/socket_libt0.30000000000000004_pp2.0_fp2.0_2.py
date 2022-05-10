import socket
import threading
import time
import sys

# 客户端
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.username = '匿名'
        self.is_login = False
        self.is_register = False
        self.is_exit = False
        self.is_connect = True
        self.is_room = False
        self.is_start = False
        self.is_end = False
        self.is_game = False
        self.is_win = False
        self.is_lose = False
        self.is_tie = False
        self.is_ready = False
        self.is_again = False
        self.is_quit = False
        self.is_leave = False
        self.is_logout = False
        self.is_exit = False
