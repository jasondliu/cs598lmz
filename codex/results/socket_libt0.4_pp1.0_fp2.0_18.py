import socket
import sys
import time
import threading
import os
import datetime
import json
import random
import string
import re
import logging
import logging.handlers
import traceback
import subprocess
import platform
import signal
import argparse
import hashlib

from contextlib import closing
from socket import error as socket_error
from collections import deque

#
#   Globals
#

#   Version
VERSION = "1.0.0"

#   Logging
LOG_LEVEL = logging.INFO
LOG_MAX_BYTES = 1048576
LOG_BACKUP_COUNT = 5

#   Command line args
ARGS = None

#   Server
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000
SERVER_TIMEOUT = 0.5
SERVER_MAX_CONNECTIONS = 10
SERVER_MAX_MESSAGE_SIZE = 1024
SERVER_MAX_MESSAGE_QUEUE = 100

#   Client
CLIENT_TIMEOUT = 0.5
CLIENT_MAX
