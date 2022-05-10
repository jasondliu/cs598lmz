import socket
import sys
import os
import time
import threading
import random
import hashlib
import base64
import json
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

# Global variables

# AES key
key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# AES counter
ctr = Counter.new(128)

# AES cipher
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

# AES initialization vector
iv = Random.new().read(AES.block_size)

# AES ciphertext
ciphertext = ''

# AES plaintext
plaintext = ''

# AES mode
mode = ''

# AES mode
mode = ''

# AES mode
mode = ''

# AES mode
mode = ''

# AES mode
mode = ''

# AES mode
mode = ''

# AES
