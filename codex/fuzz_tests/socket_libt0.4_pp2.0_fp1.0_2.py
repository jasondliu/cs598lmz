import socket
import sys
import time
import threading
import os
import json
import random
import argparse
import signal
import subprocess

from pprint import pprint

from p2p_lib import *

# Constants

# This is the port number for the P2P network
P2P_PORT = 50000

# This is the port number for the RPC network
RPC_PORT = 50001

# This is the port number for the RPC server
RPC_SERVER_PORT = 50002

# This is the port number for the RPC client
RPC_CLIENT_PORT = 50003

# This is the number of seconds between heartbeats
HEARTBEAT_INTERVAL = 5

# This is the number of seconds between attempts to connect to the
# bootstrap node
BOOTSTRAP_INTERVAL = 5

# This is the number of seconds between attempts to reconnect to the
# RPC server
RPC_SERVER_INTERVAL = 5

# This is the number of seconds between attempts to reconnect to the
# RPC client
RPC_CLIENT_INTERVAL = 5
