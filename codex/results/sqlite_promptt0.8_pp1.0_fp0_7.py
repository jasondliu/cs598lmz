import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")
import time
import os
from time import sleep
from datetime import datetime
import sys


def main():
    shell_cmd("ifconfig")
    #shell_cmd("ifconfig | grep \"ether\" | cut -d \" \" -f 2 > log_ether.txt")
    #shell_cmd("ifconfig | grep \"the\"")
    #shell_cmd("netstat -rn")  # route | grep default -> show default route
    #shell_cmd("route -n | grep \"UG\"")
    #shell_cmd("route add -net 192.168.100.0 netmask 255.255.255.0 dev eth0")

    #shell_cmd("curl -i 192.168.100.1:8081")
    #shell_cmd("curl -i 192.168.100.1:8081 -d \'{"""sensors":[{"sensorsID" : 1, """\""temp\"" : 20.3 , ""\"time\"" : "\""2014-02-02 00:00:01\""}]}\'")
    #shell_
