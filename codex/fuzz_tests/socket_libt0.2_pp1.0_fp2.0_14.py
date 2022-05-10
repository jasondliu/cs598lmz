import socket
import sys
import time
import threading
import random
import os
import signal

# Global variables

# The port number is passed in as a command line argument
port = int(sys.argv[1])

# The maximum number of connections to the server
max_connections = 5

# The maximum number of messages that can be sent to the server
max_messages = 10

# The maximum number of characters in a message
max_message_length = 100

# The maximum number of characters in a username
max_username_length = 10

# The maximum number of characters in a password
max_password_length = 10

# The maximum number of characters in a room name
max_room_name_length = 10

# The maximum number of characters in a message
max_message_length = 100

# The maximum number of characters in a username
max_username_length = 10

# The maximum number of characters in a password
max_password_length = 10

# The maximum number of characters in a room name
max_room_name_length = 10

# The maximum number of
