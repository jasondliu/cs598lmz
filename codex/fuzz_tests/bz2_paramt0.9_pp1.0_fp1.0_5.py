from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor

from io import BytesIO
BytesIO = BytesIO

from subprocess import CalledProcessError
CalledProcessError = CalledProcessError

try:
	from Crypto.Hash import SHA254
	SHA254 = SHA254
except ImportError:
	from Crypto.Hash import SHA256 as SHA254

try:
	from Crypto.PublicKey import RSA
	RSA = RSA
except ImportError:
	from Crypto.PublicKey import RSA as RSA

try:
	from Crypto.Cipher import PKCS1_v1_5
	PKCS1_v1_5 = PKCS1_v1_5
except ImportError:
	from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5

try:
	import certs as x509
	x509 = x509
except ImportError:
	import ssl as x509

try:
	from OpenSSL import crypto
	crypto = crypto
except ImportError:
	from M2Crypto import crypto

try:
	from argparse import ArgumentParser

