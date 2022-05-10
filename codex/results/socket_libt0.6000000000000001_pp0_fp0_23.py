import socket
import sys
import os
import uuid
import random
import string
import re

def help():
    print("""
    Usage:
        python3 plc_client.py [hostname] [port] [method] [args]

        [hostname] - hostname of the plc to connect to
        [port] - port of the plc to connect to
        [method] - method to call on the plc
        [args] - args to pass to the method

        Examples:
            python3 client.py localhost 1729 read_memory 0x0 0x10
            python3 client.py localhost 1729 write_memory 0x0 0x10 0x41414141414141414141414141414141
            python3 client.py localhost 1729 write_memory 0x0 0x10 AAAAAAAAAAAAAAAAAAAAAAAA
            python3 client.py localhost 1729 read_file /etc/passwd 0x0 0x10
            python3 client.py localhost 1729 write_file /tmp/test.txt 0x0 0x10 AAAAAAAAAAAAAAAAAAAAAAAA
           
