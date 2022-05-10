import socket
import sys
import time
import thread
import time
import threading
import os
import re
import Queue
import struct
import random
import datetime
import logging

from Src.Server import Server
from Src.Message import Message
from Src.Log import Log
from Src.Client import Client
from Src.Usr import Usr
from Src.DBConn import DBConn
from Src.Server import Server

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    usr_queue = Queue.Queue()
    threading.Thread(target=Server.worker_thread, args=(usr_queue, '127.0.0.1', 0)).start()
    time.sleep(1)
    print('Server is running at port: ' + str(Server.get_port()))
