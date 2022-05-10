import select
import sys
import multiprocessing
import sys
import socket
import select
import datetime
import paramiko
import hashlib
try:
    import Crypto
    import Crypto.Random
    from Crypto.PublicKey import RSA
except ImportError:
    print('Paramiko requires pycrypto >= 2.6')
    sys.exit(1)

__author__ = 'jacuswinkle@gmail.com'


def rng_func(n):
    return Crypto.Random.get_random_bytes(n)


def get_key():
    try:
        with open('/root/.ssh/id_rsa') as f:
            pkey = paramiko.RSAKey(file_obj=f)
    except IOError as e:
        print('Generating new ssh key: %s' % e)
        key = paramiko.RSAKey.generate(2048, rng_func)
        secret = key.get_base64()
        hash_secret = hashlib.sha256(secret.encode('utf-8')).hexdigest()
