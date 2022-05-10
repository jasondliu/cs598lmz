import socket
import select
import sys
import os
import pickle
import logging
import _thread
from exceptions import ValueError

BUFFER_SIZE = 1024
current_dir = os.path.dirname(os.path.realpath(__file__))

def client_thread(conn,client_addr):
    file_name = ''
    file_name_received = True
    data = ''

