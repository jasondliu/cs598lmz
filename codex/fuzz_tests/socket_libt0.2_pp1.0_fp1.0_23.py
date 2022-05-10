import socket
import sys
import time
import threading
import os
import subprocess
import re

# Global variables

# IP address of the server
server_ip = "127.0.0.1"
# Port number of the server
server_port = 8080
# Port number of the client
client_port = 8081
# IP address of the client
client_ip = "127.0.0.1"
# List of all the files in the directory
files = []
# List of all the files in the directory with their last modified time
files_time = []
# List of all the files in the directory with their last modified time and their size
files_time_size = []
# List of all the files in the directory with their last modified time and their size and their hash
files_time_size_hash = []
# List of all the files in the directory with their last modified time and their size and their hash and their version
files_time_size_hash_version = []
# List of all the files in the directory with their last modified time and their size and their hash and their version and their status
files_time
