import select
import socket
import sys
import time
import threading
import logging
import logging.handlers

logger = logging.getLogger('socket_server')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('/var/log/socket_server.log', maxBytes=1024*1024*10, backupCount=5)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(fh)
logger.addHandler(ch)

#logging.basicConfig(filename='/var/log/socket_
