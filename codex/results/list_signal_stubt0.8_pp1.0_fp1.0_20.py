import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
print('Start.')
while delays:
    signal.pause()



# #!/usr/bin/env python3
# # Foundations of Python Network Programming, Third Edition
# # https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# # UDP client and server for talking over the network
#
# import argparse, random, socket, sys
# from datetime import datetime
#
# MAX_BYTES = 65535
#
#
# def server(interface, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((interface, port))
#     print('Listening at', sock.getsockname())
#     while
