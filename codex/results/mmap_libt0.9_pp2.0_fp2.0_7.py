import mmap
import os
import sys
symbol_name = '.data'
symbol_line = int(sys.argv[2])

f = open(sys.argv[1], 'r+b')
nmap = mmap.mmap(f.fileno(), 0)
symbol_offset = int(os.popen("objdump -t driver.o | grep '%s' | cut -d' ' -f1"%(symbol_name)).read(),16)
print symbol_offset
symbol_offset += symbol_line
print symbol_offset
nmap.seek(symbol_offset)
nmap.write(chr(0x0))
nmap.close()
f.close()
