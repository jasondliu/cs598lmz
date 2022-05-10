import socket
import sys
import time

from lidar_lite import Lidar_Lite
from simple_pid import PID

from fn_control import *


lidar = Lidar_Lite()
connected = lidar.connect(1)

def main():
    # Send info to the server
    server_address = ('10.200.4.4', 5678)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    pid = PID(0, 0.01, 0, setpoint=30)
