import select
import sys
import time
import logging
import thread
import json
import signal
import sys
import socket
import rpyc
import os
import os.path
import math
import traceback

logging.basicConfig(filename="client.log", level=logging.INFO)

# Function to handle ctrl+c
