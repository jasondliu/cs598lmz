import socket
import time
import threading
import sys
import json
import pickle
import struct
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Global variables

# Constants
KEY = "abcdefghijklmnop"
IV = "abcdefghijklmnop"
PORT = 8080
SIZE = 1024

# Arrays
clients = []
keys = []
ivs = []

# Strings
key = ""
iv = ""

# Booleans
is_server = False

# Methods

# Generate a key and an IV
def gen_key_iv():
    global key, iv
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

# Encrypt a message with the given key and IV
def encrypt(message):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(message, AES.block_size))


