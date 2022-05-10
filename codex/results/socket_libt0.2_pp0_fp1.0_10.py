import socket
import sys
import time
import threading
import os
import signal
import subprocess
import re
import json
import random
import string
import base64

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

# Global variables

# The port on which to listen
listenPort = 9999

# The public and private keychains in PEM format
publicKeyChain = 'public.pem'
privateKeyChain = 'private.pem'

# The cipher for encrypting messages sent to the client
serverCipher = None

# The cipher for decrypting messages sent by the client
clientCipher = None

# The cipher for encrypting messages sent to the server
clientCipher = None

# The cipher for decrypting messages sent by the server
serverCipher = None

# The cipher for encrypting messages sent to the server
clientCipher = None

# The cipher for decrypting messages sent by the server
server
