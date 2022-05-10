import ctypes
import ctypes.util
import threading
import sqlite3
import re
import requests
import urllib.parse
import time
import sys
import json
import os
import urllib.request
from config import *

if not os.path.exists("data"):
    os.mkdir("data")

def getTime():
    return time.time()*1000

def getTimeString():
    return time.strftime("%Y-%m-%d %H:%M:%S.%f",time.localtime(time.time()))

def getTimeStringWithoutMillisecond():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

class BilibiliLiveDanMuHelper:
    def __init__(self,roomid,debug=False,url=None):
        self.is_live = False
        self.roomid = roomid
        self.url = url
        self.debug = debug
        self.live_url = "https://api.live.bilibili.com/room/v1/
