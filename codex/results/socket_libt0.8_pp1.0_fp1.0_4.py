import socket
import time
import logging
import argparse
import sys
from threading import Thread

from constants import *
from util import get_ip_address, init_logging
from messenger import Messenger
import address_book


class Node:

    def __init__(self, config_file=None, address_book_file=None, debug=False, **kwargs):
        self.debug = debug

        self.is_running = True
        self.sender_addr = (get_ip_address(), 0)

        # initialize the logger
        self.logger = init_logging(debug, kwargs['log_file'])

        # initialize the configuration
        self.config = self.init_config(config_file, kwargs)

        # initialize the address book
        self.address_book = address_book.AddressBook(address_book_file)

        # initialize socket
        self.init_socket(self.config['port'])

        # initialize messenger
        self.messenger = Messenger(self.socket, self.address_book, logger=self.logger)

       
