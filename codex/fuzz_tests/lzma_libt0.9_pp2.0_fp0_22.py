import lzma
lzma.decompress(s).decode()

#%%
s = bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

bs = b''
for i in s:
    bs += bytes.fromhex(hex(i)[2:])
bs

#%%
import base64
base64.b64encode(s)

#%%
import string
from itertools import cycle

class RepeatingXOR(object):
    def __init__(self, key):
        self.key = str(key).encode('utf-8')
        self.cycle = cycle(self.key)
        self.table = self.enc_table()
        self.dtable = self.dec_table()
        
    def enc_table(self):
        table = dict()
        for i, char in enumerate(self.key):
            for j, letter in enumerate
