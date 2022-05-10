import ctypes
import ctypes.util
import threading
import sqlite3
import urllib
import urllib2
import json
import socket
import os
import time
import fcntl
import datetime
import urlparse

# Settings
#---------
Notify_SMS_Range = [8,23]
Notify_SMS_MaxCount = 1
IP_Address = '192.168.1.78'
WPS_Config = "/etc/wpa_supplicant/wpa_supplicant-wlan0.conf"
Interface = 'wlan0'
RSSI_Limit = -80
Pokecat_API = "http://pokecat.info:3333/api/ap/nearby"
#---------

SCAN_RESULT_MTU = 4096
SIOCSIWENCODE = 0x8B2A
SIOCGIWSCAN = 0x8B18
SIOCGIFADDR = 0x8915

CHECK_INTERVAL_SECONDS = datetime.timedelta(hours=1)

scanner_started = False
notify_sms_counter = 0
notify_sms_limit
