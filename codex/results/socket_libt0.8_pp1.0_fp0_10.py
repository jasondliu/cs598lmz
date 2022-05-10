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

    while True:
        try:
            if file_name_received:
                file_name = conn.recv(BUFFER_SIZE)
                if os.path.exists(file_name):
                    file_name_received = False
                    conn.send(pickle.dumps(200))
                    logging.info('%s:%s: File: %s found.' % (client_addr[0], client_addr[1], file_name))
                else:
                    conn.send(pickle.dumps(404))
                    logging.info('%s:%s: File: %s not found.' % (client_addr[0], client_addr[1], file_name))
           
