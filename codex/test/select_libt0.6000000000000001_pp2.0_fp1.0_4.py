import selectors
import json
import queue
import pickle
import re
import os
import time


class Client:
    def __init__(self):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__selector = selectors.DefaultSelector()

        self.__client_socket.setblocking(False)
        self.__selector.register(self.__client_socket, selectors.EVENT_READ, self.__handle_data_received)

        self.__client_socket.connect(('localhost', 5555))
        # self.__client_socket.connect(('172.20.10.2', 5555))

        self.__message_queue = queue.Queue()
        self.__is_connected = True

        self.__message_handler = MessageHandler(self.__message_queue)

    def __handle_data_received(self, connection_socket, mask):
        try:
            data = connection_socket.recv(1024)
        except Exception:
            data = None

       
