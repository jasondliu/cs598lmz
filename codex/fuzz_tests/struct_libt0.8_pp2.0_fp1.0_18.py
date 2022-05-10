import _struct
import socket
from netaddr import IPNetwork, IPAddress
from pcapy import open_live, findalldevs
from os import popen
from sys import argv,exit
import threading
import signal
from time import sleep
from optparse import OptionParser
import time
from multiprocessing import Process, Queue, Value
from operator import itemgetter
import sqlite3

class class_arp:
    def __init__(self, ip, mac, interface):
        self.ip = ip
        self.mac = mac
        self.interface = interface
        self.last_time = time.time()
        self.last_pos = 0
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return "[IP: %s MAC: %s Interface: %s]" % (self.ip, self.mac, self.interface)

class Sniffer(threading.Thread):
    def __init__(self, filter, iface, queue, name, close_event, arp_table):
       
