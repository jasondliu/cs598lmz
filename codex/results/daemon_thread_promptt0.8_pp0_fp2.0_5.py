import threading
# Test threading daemon
#from time import sleep
#from random import randrange

from shared import Event_Withdraw
from shared import Event_Server_Msg

# This file contains the server logic.

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: If change to localhost, change to 127.0.0.1
server_socket.bind(('0.0.0.0', 65432))

# Queue up to 5 requests
server_socket.listen(5)

# Get the initial time
TIME = time.time()

print("Server Initializing...")

# The class for each individual client
class Client_Thread(threading.Thread):
    # The associated socket for each thread
    sock = None
    # The associated username for each thread
    usern = ""

    def check_sock(self, s):
        if s in clients:
            return True
        else:
            return False

    # Initializes the Client_Thread
    def __init__(self, socket, username
