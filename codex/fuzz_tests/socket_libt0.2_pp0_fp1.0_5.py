import socket
import sys
import time
import threading
import os
import re
import json
import random
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

# Global variables
global_key = ""
global_iv = ""
global_counter = ""
global_cipher = ""
global_cipher_mode = ""
global_cipher_block_size = 0
global_cipher_key_size = 0
global_cipher_iv_size = 0
global_cipher_counter_size = 0
global_cipher_name = ""
global_cipher_mode_name = ""
global_cipher_padding = ""
global_cipher_padding_name = ""
global_cipher_padding_size = 0
global_cipher_padding_block_size = 0
global_cipher_padding_block_size_in_bits = 0
global_cipher_padding_block_size_in_bytes = 0
global_cipher_padding_block_size_in_hex = ""
global_cipher_padding_block_
