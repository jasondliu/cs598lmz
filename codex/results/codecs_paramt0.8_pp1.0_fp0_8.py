import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# Import pycryptodome
#from Crypto.Cipher import ARC4
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util import Counter

# Import other internal dependencies
from utils import *
from config import *
from defines import *

VPT_CIPHER_ALGORITHM = 'AES'
VPT_HASH_ALGORITHM = 'SHA256'

def cipher_init(cipher_algorithm, mode, key, iv, counter):
	global VPT_CIPHER_ALGORITHM
	global VPT_HASH_ALGORITHM

	if cipher_algorithm == VPT_CIPHER_ALGORITHM:
		if mode == 'CBC':
			return AES.new(key, AES.MODE_CBC, iv)
		elif mode == 'CTR':
			return AES.new(key, AES.MODE_CTR, counter=counter)
		else:
		
