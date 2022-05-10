import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import threading
import atexit
import logging
import traceback


def main():
    # config = ConfigParser.RawConfigParser()
    # config.read('config.cfg')
    #
    # config_path = config.get('Path', 'config_path')
    # log_path = config.get('Path', 'log_path')
    #
    # log_name = config.get('Log', 'log_name')
    # log_level = config.get('Log', 'log_level')
    #
    # log_file = os.path.join(log_path, log_name)
    #
    # logging.basicConfig(filename=log_file,
    #                     filemode='a',
    #                     level=logging.DEBUG,
    #                     format='%(asctime)s %(process)d %(levelname)s %(message)s')
    #
    # logging.info('Starting %s'
