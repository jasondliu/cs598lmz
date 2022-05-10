import socket
import datetime
import time
import sys
import threading
import argparse
import logging
import logging.handlers
import os

def update_thread(sock, address, port, interval):
    try:
        sock.settimeout(2)
        while True:
            logging.info('Sending update to ' + address + ':' + str(port))
            sock.sendto('UPDATE', (address, port))
            time.sleep(interval)
    except Exception, e:
        logging.error('Error sending update to ' + address + ':' + str(port) + ': ' + str(e))

def start_update_thread(sock, address, port, interval):
    update_thread_ = threading.Thread(target=update_thread, args=(sock, address, port, interval))
    update_thread_.daemon = True
    update_thread_.start()

def main(args):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_S
