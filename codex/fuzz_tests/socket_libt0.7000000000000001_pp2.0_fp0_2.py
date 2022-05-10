import socket
import sys
import time
import thread
import urllib2

# Python 2.x backward compatibility hacks
if sys.version_info.major < 3:
    import SocketServer
    import BaseHTTPServer
    if sys.version_info.minor < 6:
        import SimpleHTTPServer
    else:
        import http.server as SimpleHTTPServer
else:
    import socketserver as SocketServer
    import http.server as BaseHTTPServer
    import http.server as SimpleHTTPServer
    raw_input = input

# Constants
DEFAULT_PORT = 8000
TIMEOUT = 60

# Globals
clients = []
messages = []

# Command handlers
def handler_help(args):
    return "Available commands: " + ", ".join(cmd_handlers.keys())

def handler_quit(args):
    return "bye!"

def handler_name(args):
    client["name"] = args[0]
    return "your name is: " + client["name"]

def handler_say(args):
    msg = " ".join
