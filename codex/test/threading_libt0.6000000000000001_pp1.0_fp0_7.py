import threading
threading.stack_size(500000)

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import SHA1
from Crypto.Hash import HMAC
from Crypto import Random
import base64
import csv
import json
import os
import sys

# AES key, HMAC key, and IV to use for encryption and HMAC
KEY = Random.new().read(AES.block_size)
HMAC_KEY = Random.new().read(SHA256.block_size)
IV = Random.new().read(AES.block_size)

# A dictionary of all the encrypted columns
