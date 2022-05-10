import socket
import sys
import time
import datetime
import os

# create dirs
base_dir = '/var/www/html/logs/'
today_dir = base_dir + datetime.datetime.now().strftime("%Y%m%d")
if not os.path.exists(today_dir):
    os.makedirs(today_dir)

# create logger
logger = logging.getLogger("server")
logger.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler(today_dir + '/' + datetime.datetime.now().strftime("%H") + '.log')
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# add formatter to ch
fh.setFormatter(formatter)

# add fh to logger
logger.addHandler(fh)

HOST = ''
PORT = 8888
BU
