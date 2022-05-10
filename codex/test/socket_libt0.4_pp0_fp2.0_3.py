import socket
import threading
import time
import datetime
import random

# def get_host_ip():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(('8.8.8.8', 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#     return ip

def get_host_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_random_number():
    return random.randint(1, 100)

def get_data(data_type):
    if data_type == "time":
        return get_time()
    elif data_type == "random":
        return get_random_number()
    else:
        return "unknow"

