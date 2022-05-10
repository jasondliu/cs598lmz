import socket
import sys
import time
import threading
import random
import os
import signal
import re
import datetime

# Global variables

# The name of the file to be used for logging chat messages
LOG_FILE_NAME = "chatroom.log"

# The server's hostname or IP address
SERVER_HOST = 'localhost'

# The server's port
SERVER_PORT = 1234

# The string to send to the server, requesting the list of the names of the
# people currently in the chat room
LIST_USERS_MESSAGE = "\xF0\x9F\x93\xB1"

# The string to send to the server, requesting the names of the people in the
# chat room, followed by a list of the names of people to whom the client wishes
# to send private messages
PRIVATE_MESSAGE_REQUEST = "\xF0\x9F\x93\xB2"

# The string to send to the server, informing it that the client is disconnecting
DISCONNECT_MESSAGE = "\xF0
