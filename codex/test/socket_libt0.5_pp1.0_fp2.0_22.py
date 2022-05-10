import socket
import time
import sys
import os
import subprocess
import re
import signal
import datetime
import logging
import logging.handlers

# Global variables
#
#
#
#
#
#
#

# Logging
logger = logging.getLogger('myapp')
hdlr = logging.handlers.RotatingFileHandler('/var/log/backup.log', maxBytes=1000000, backupCount=5)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
