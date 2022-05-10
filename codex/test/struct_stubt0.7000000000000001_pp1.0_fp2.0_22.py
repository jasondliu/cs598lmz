from _struct import Struct
s = Struct.__new__(Struct)
s.format_str = "<I"
s.size = 4
def to_struct(x):
    return x.to_bytes(32, 'big')
def from_struct(b):
    return int.from_bytes(b, 'big')

def generate_keypair():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def get_pubkeyhash(public_key):
    public_key_bytes = public_key.to_string()
    sha = hashlib.sha256(public_key_bytes)
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha.digest())
    return ripemd.digest()

def get_address(public_key):
    pubkeyhash = get_pubkeyhash(public_key)
    hash160 = bytes.fromhex('00') + pubkeyhash
   
