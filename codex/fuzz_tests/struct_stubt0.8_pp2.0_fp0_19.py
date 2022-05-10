from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hi')


#pype32.PE.from_bytes(open('stub1.dat', 'rb').read())

with open('stub1.dat', 'rb') as f:
    p = pype32.PE.from_stream(f)
#p.get_memory_mapped_image()

#print(p.dump_info())
with open('stub1.dat', 'rb') as f:
    d = pype32.PE.from_stream(f).dump_info()
    
    
    
    
import os
import pefile
import peutils
import sys

pe = pefile.PE('stub1.dat')
sig_db =  peutils.SignatureDatabase('UserDB.TXT')
matches = sig_db.match(pe, ep_only = True)

print(matches)

#print(os.listdir('.'))

import os
import zipfile
import rarfile



#    with open('stub1.dat', 'rb') as f:
