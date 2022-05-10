import socket
socket.if_indextoname(2)

import csv
import copy
import time
import logging
import argparse
import os
import re

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

from scapy.all import *
import psutil
import matplotlib.animation as animation

import multiprocessing
from multiprocessing import Process
from multiprocessing.connection import Listener

# custom modules
import dns_sniff
import dns_query
import bandwidth_sniff
import bandwidth_query
import bandwidth_sniff_parsed
import bandwidth_query_parsed
import geoloc


class Monitor:
    def __init__(self):
        self.monitoring = False
        self.monitor_thread = None
        self.dns_monitoring = False
        self.dns_monitor_thread = None
        self.geoloc_monitoring = False
        self.geoloc_monitor_thread
