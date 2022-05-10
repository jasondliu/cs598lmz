import threading
# Test threading daemon
import time
import sys
import os
import subprocess
import signal

# import the logging library
import logging
import logging.handlers

# Get the arguments
import argparse

# Get the config
import configparser

# Get the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Set the logger
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.handlers.RotatingFileHandler('main.log', maxBytes=10000, backupCount=5)
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Starting the program')

# Get the arguments
parser = argparse.ArgumentParser(description='Process some integers.'
