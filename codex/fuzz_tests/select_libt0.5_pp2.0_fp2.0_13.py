import select
import socket
import sys
import termios
import tty

from . import config
from . import control
from . import utils

def main():
    parser = argparse.ArgumentParser(description='Control a robot')
    parser.add_argument('--config', default='config.py',
                        help='Specify a different configuration file')
    parser.add_argument('--host', default='localhost',
                        help='Hostname to connect to')
    parser.add_argument('--port', default=8000, type=int,
                        help='Port to connect to')
    args = parser.parse_args()
    config.load_config(args.config)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host, args.port))
    fd = sock.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    try:
        while True:
            r, _, _ = select.select([sys.stdin, sock
