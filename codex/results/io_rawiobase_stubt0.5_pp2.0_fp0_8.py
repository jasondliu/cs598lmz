import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        data = self.file.read(n)
        if len(data) != n:
            raise EOFError()
        b[:len(data)] = data
        return len(data)

import random
#from Crypto.Cipher import AES
from Crypto.Cipher import AES
import struct
import hashlib
from Crypto.Util import Counter

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Hash import HMAC

import os
import sys
import time
import threading
import logging
import json
import random
import base64
import socket
import selectors
import traceback
import pymysql
import pym
