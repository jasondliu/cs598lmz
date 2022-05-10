import select
from time import time
import json
from time import time
from struct import pack, unpack
from urllib.parse import urlparse
import base64
import requests
from kafka import KafkaConsumer

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from dtls import do_patch
from dtls.error import WantReadError, WantWriteError
from dtls.ssl import SSLContext, SSLSocket
from dtls.ssl_ import SSL_ERROR_WANT_READ, SSL_ERROR_WANT_WRITE

from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI

do_patch()

# Information about the DTLS peer we are connecting to
SERVER_HOSTNAME = "127.0.0.1"
SERVER_PORT = 5684

# Information about the DTLS peer we are connecting to
SERVER_HOSTNAME = "127.0.0.1"
SERVER_PORT
