import threading
# Test threading daemon
from service import get_messages
import time


#####
# SETUP:
#
#   - Start this script, and then open the client.html in a web browser.
#   - Send a message from the web browser to the server. Try this a few
#     times. You should see each message appear on the server console.
#   - Try refreshing the web browser. You should see the messages
#     disappear from the server console, and then re-appear.
#####

HOST, PORT = '', 8888

# Globals
handlers = []

def create_server():
    """Creates and returns an instance of the server."""
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.timeout = 0.3
    server.daemon_threads = True
    return server


class MyTCPHandler(socketserver.BaseRequestHandler):
    """Handle incoming messages from clients.

    Messages are appended onto the messages list as tuples, of the form:
        (client_address, message)

   
