import mmap
import os

from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsError
from kazoo.handlers.threading import SequentialThreadingHandler
from kazoo.recipe.watchers import ChildrenWatch, DataWatch

import sys
import logging
logging.basicConfig()
import colorama
colorama.init()

from pbkdf2 import crypt
from pbkdf2 import pbkdf2

from hashlib import md5
from hashlib import sha1
from scrypt import scrypt

from Crypto.Cipher import AES

from utils import *

# Exceptions
# The key and/or initialization vector are not valid
class InvalidKeyOrIV(Exception):
    pass

# The hash algorithm is not supported
class InvalidHashAlgorithm(Exception):
    pass

# The encryption algorithm is not supported
class InvalidEncryptionAlgorithm(Exception):
    pass

# The key length is not valid
class InvalidKeyLength(Exception):
    pass

# The input is not valid
class InvalidInput(Exception):
