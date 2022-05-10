import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import base64
import binascii
from Crypto.Cipher import AES
import hashlib
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.Cipher import AES



# Global Variables

# AES key
AES_KEY = "D9D9D9D9D9D9D9D9"

# RSA public key
RSA_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoLlQ2dS0uzbv+7pJ4A4A\n4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x4x\n4x4x4x4x4x4x4x
