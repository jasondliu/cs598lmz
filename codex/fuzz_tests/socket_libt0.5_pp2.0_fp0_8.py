import socket
import argparse
import time
import threading
import random

# Arguments
parser = argparse.ArgumentParser(description='Start a simple TCP server')
parser.add_argument('port', type=int, help='Port to listen on')
parser.add_argument('--ip', default='0.0.0.0', help='IP address to listen on')
parser.add_argument('--max-clients', default=10, type=int, help='Maximum number of simultaneous connections')
parser.add_argument('--max-conn-time', default=60, type=int, help='Maximum time (in seconds) a connection is allowed to stay open')
parser.add_argument('--max-msg-size', default=1024, type=int, help='Maximum message size (in bytes)')
parser.add_argument('--msg-delay', default=0, type=float, help='Time (in seconds) to wait between messages')
parser.add_argument('--msg-timeout', default=5, type=float, help='Time (in seconds) to wait for a message to arrive')
parser.add
