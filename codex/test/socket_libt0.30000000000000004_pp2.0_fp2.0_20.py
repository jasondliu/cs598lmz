import socket
import sys
import time
import threading
import random
import os
import struct
import hashlib

# 定义一个类，表示一个用户信息
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

# 定义一个类，表示一个用户登录信息
class User_login:
    def __init__(self, name, password, ip, port):
        self.name = name
        self.password = password
        self.ip = ip
        self.port = port

# 定义一个类，表示一个群组信息
class Group:
    def __init__(self, group_name, group_id, group_owner, group_member):
        self.group_name = group_name

