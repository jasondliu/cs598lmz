import socket
import sys
from threading import Thread
from queue import Queue
from queue import LifoQueue
import random
import time
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)


send_queue = LifoQueue()


# def job(q):
#     while True:
#         args = q.get()
#         message_dict = args
#         templ = '!'+'B'+''.join(['i' for num in range(len(message_dict))])
#         send_str = struct.pack(templ, *message_dict.values())
#         print(message_dict)
#         # print(send_str)
#         sock.sendall(send_str)
#         q.task_done()
