import socket
import time
import os
import copy
import logging
import signal
import sys
import struct
import ipaddress

from params import params


# logging
args = params()
logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', level=args.log_level)

# create SIGINT handler
def handle_sigint(sig, frame):
    if (thread1.is_alive()):
        logging.info("server thread got SIGINT and is terminating")
        sys.exit(0)


def handler(signum, frame):
    logging.info("handler called")
    logging.info(signum, frame)
    sys.exit(0)


# set handler for SIGINT
signal.signal(signal.SIGINT, handle_sigint)

# setup the network
ip_address = args.ip_address
ip_address_list = ipaddress.ip_address(ip_address)
logging.debug(ip_address_list)
ip_address_list.reverse()

