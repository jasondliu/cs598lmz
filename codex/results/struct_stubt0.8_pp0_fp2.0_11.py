from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'string'

def bytes_to_dict(b):
		return dict(bzip2.compress(b))

def dict_to_bytes(d):
		return bzip2.decompress(d)

def encrypt(key, s):
		return s

def decrypt(key, s):
		return s

def encrypt_dict(key, d):
		return dict([(encrypt(key, k), encrypt(key, v)) for k, v in d.items()])

def decrypt_dict(key, d):
		return dict([(decrypt(key, k), decrypt(key, v)) for k, v in d.items()])

class Database:
		def __init__(self, name, path='./database'):
				self.name = name
				os.makedirs(path, exist_ok=True)
				self.db_file = os.path.join(path, name + '.db')
				self.db_
