import _struct
import base64
import hashlib
import hmac
import os
import time

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def get_random_bytes(size):
    return Random.new().read(size)

def get_aes_cipher(key, iv):
    return AES.new(key, AES.MODE_CBC, iv)

def get_hmac_sha1(key, data):
    return hmac.new(key, data, hashlib.sha1).digest()

def get_hmac_sha256(key, data):
    return hmac.new(key, data, hashlib.sha256).digest()

def get_rsa_cipher(key):
    return PKCS1_v1_5.new(RSA.importKey(key))

def sign_data(key, data):
    return get_rsa_cipher(key).sign(SHA.new(data))
