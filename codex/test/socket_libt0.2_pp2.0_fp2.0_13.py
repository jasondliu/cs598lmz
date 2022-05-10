import socket
import sys
import time
import threading
import os
import random
import string
import json
import base64

from Crypto.Cipher import AES
from Crypto import Random

# This is the server's IP address
HOST = '127.0.0.1'

# This is the server's port
PORT = 1234

# This is the maximum number of connections that can be queued
MAX_CONNECTIONS = 5

# This is the size of the buffer
BUFFER_SIZE = 1024

# This is the number of bytes in the AES key
KEY_SIZE = 32

# This is the number of bytes in the AES IV
IV_SIZE = 16

# This is the number of bytes in the AES block
BLOCK_SIZE = 16

# This is the number of bytes in the AES padding
PADDING_SIZE = 16

# This is the number of bytes in the AES padding
PADDING_CHAR = '\x00'

# This is the number of bytes in the AES padding
PADDING_CHAR_ORD = 0

# This is the number of bytes in the
