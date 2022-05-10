import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import dpkt
import pcap
import sys
import os
import urllib2
import gzip
import shutil

import client


def log(message):
    print(str(message))


class Mapper:

    def __init__(self):
        self.lock = threading.Lock()

        self.ip_info = self.get_ip_info()
        self.geo_data = self.get_geo_data()
        self.geo_data_loaded = False

        self.session = self.connect_to_db()

    @staticmethod
    def parse_ip_info():
        log('Parsing ip_info')

        ip_info = {}
        ip_info_f = open(client.IP_INFO_LOCATION, 'rb')
        for line in ip_info_f.readlines():
            split_list = line.split('|')
            # Second to last is the ASN
            ip_info[split_list[0]] = split_list[-2]
        ip_
