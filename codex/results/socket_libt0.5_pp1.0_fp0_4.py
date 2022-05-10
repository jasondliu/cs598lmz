import socket
import time
import sys
import os
import re
import getpass
import traceback

from . import constants
from . import util
from . import server
from . import client
from . import config

def run_client(args):
    if not args.server:
        print("--server is required")
        return 1
    if not args.port:
        print("--port is required")
        return 1
    if not args.id:
        print("--id is required")
        return 1
    if not args.password:
        print("--password is required")
        return 1

    client.main(args.server, args.port, args.id, args.password)

def run_server(args):
    if not args.port:
        print("--port is required")
        return 1
    if not args.password:
        print("--password is required")
        return 1
    if not args.key:
        print("--key is required")
        return 1
    if not args.cert:
        print("--cert is required")
        return 1


