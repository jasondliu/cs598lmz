import socket
import time
import threading
import random
import sys
import os

# ---------------------------
# @description 
# @author xichengxml
# @date 2019/10/14 下午 05:50
# ---------------------------


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_host_name():
    return socket.gethostname()


def get_host_mac():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
    except Exception as e:
        return "00:00:00:00:00:00"


