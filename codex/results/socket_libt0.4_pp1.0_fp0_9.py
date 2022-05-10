import socket
import sys
import threading
import time
import random
import os

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_int(length):
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return int(result_str)

def get_random_ip():
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def get_random_mac():
    return ':'.join(map(lambda x: "%02x" % x, [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]))

def get_random_port():
