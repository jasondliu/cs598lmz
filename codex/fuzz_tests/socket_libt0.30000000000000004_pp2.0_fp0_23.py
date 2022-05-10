import socket
import time
import threading
import json
import sys
import os

# global variables

# client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server address
server_address = ('localhost', 10000)

# connection flag
connected = False

# username
username = ''

# list of users
users = []

# list of messages
messages = []

# list of rooms
rooms = []

# current room
current_room = ''

# list of files
files = []

# list of file names
file_names = []

# list of file sizes
file_sizes = []

# list of file owners
file_owners = []

# list of file paths
file_paths = []

# list of file types
file_types = []

# list of file ids
file_ids = []

# list of file upload times
file_upload_times = []

# list of file download times
file_download_times = []

# list of file downloaders
