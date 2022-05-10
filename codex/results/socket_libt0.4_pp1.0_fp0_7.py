import socket
import threading
import time
import logging
import sys
import struct
import os
import json
import random

# 全局变量
LOCAL_IP = '127.0.0.1'
LOCAL_PORT = 8888
BUFFSIZE = 1024

# 全局队列
'''
    全局队列用于存储所有的连接对象
    其中每一个连接对象都是一个字典，包含该连接的所有信息
    包括连接的客户端的ip地址，以及该连接的socket对象
'''
connections = []

# 全局锁
lock = threading.Lock()

#
