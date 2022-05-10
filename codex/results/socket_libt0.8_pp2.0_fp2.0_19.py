import socket
import time
import random
import signal
import sys
import threading
from random_word import RandomWords

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 4444))
s.listen(5)

rw = RandomWords()

def shutdownHandler(signum, frame):
    print("Shutting down in 1 second")
    time.sleep(1)
    s.shutdown(1)
    s.close()

signal.signal(signal.SIGINT, shutdownHandler)

def validUsername(username):
    pattern = r"^[a-zA-Z][a-zA-Z0-9]+$"
    if re.match(pattern, username):
        r = rw.get_random_word(hasDictionaryDef="true")
        return r
    return None

def makeList(username, lst):
