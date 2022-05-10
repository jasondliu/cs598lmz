import selectors
import socket
import types
import sys
import os
import re
import time
import getopt
import threading
import json
import base64
import queue

# 全局变量，用于存储服务器的地址
SERVER_ADDRESS = ('localhost', 8888)

# 全局变量，用于存储客户端的地址
CLIENT_ADDRESS = ('localhost', 8889)

# 全局变量，用于存储服务器的socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 全局变量，用于存储客户端的socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 全
