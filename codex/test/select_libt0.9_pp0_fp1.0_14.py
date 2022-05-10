import select
import threading
import time
import logging
import socket
import atexit
import signal

halt=False
me=socket.gethostname()

def get_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 12162))
    #sock.setblocking(0)
    #sock.settimeout(3)
    return sock

# annoying lock to sync between print and http threads
print_lock=threading.Lock()
def get_print_lock():
    global print_lock
    return print_lock

def ping():
    sock=get_socket()
