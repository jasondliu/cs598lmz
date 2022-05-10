import bz2
bz2.decompress(bz2_filecontent)
import sys
sys.path.append('..')
from misc import lcsubstr
from misc import hextostr
from misc import bytes2xor
from misc import xorstr
from misc import get_hamming_distance
import itertools
 
import numpy as np

from PIL import Image

from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Hash import SHA, MD5
from Crypto.Cipher import AES
import random
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64

from binascii import hexlify, unhexlify
from Crypto.PublicKey import DSA
from Crypto.Util.number import long_to_bytes
from struct import pack, unpack
from hashlib import sha1

from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PK
