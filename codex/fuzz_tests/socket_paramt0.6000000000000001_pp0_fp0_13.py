import socket
socket.if_indextoname('1')

import sys
sys.path
sys.path.append("/home/david/anaconda2/lib/python2.7/site-packages")

import dpkt
import socket
import sys
import os
import threading
import time
import datetime
import random
import argparse
import subprocess
import re
import thread
import ConfigParser
import json
import Queue
import traceback
import csv

def get_packet_length(packet):
	try:
		pkt = dpkt.ethernet.Ethernet(packet)
		return len(pkt.data)
	except Exception as e:
		print e
		return 0

def get_packet_timestamp(packet):
	try:
		pkt = dpkt.ethernet.Ethernet(packet)
		return pkt.data.time
	except Exception as e:
		print e
		return 0

def get_packet_time_interval(packet1, packet2):
	
