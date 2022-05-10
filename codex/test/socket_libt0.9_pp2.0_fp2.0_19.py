import socket
import time
import threading
import os
import sys
try:
    import msvcrt    
except ImportError:
    import subprocess
    try:
        clear = lambda: subprocess.call('clear', shell=True)
    except ImportError:
        print("Your Operating System is not supported yet.")
        sys.exit()

class handler():
    def __init__(self, s, message_size):
        self.s = s
        self.message_size = message_size

    def send(self, msg, user=""):
        data = msg
        command = ''
        if (user==""):
            #send message out to everyone
            self.s.sendall(('0' + data + (self.message_size - len(data))*' ').encode('utf-8'))
            print("\r", end='')
        else:
            #send message to user
            self.s.sendall(('2' + user + (self.message_size - len(user))*' ').encode('utf-8'))
           
