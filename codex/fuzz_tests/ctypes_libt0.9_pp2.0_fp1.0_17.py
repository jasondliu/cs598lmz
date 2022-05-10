import ctypes
ctypes.CDLL('libkeystone.so', mode=ctypes.RTLD_GLOBAL)
from capstone import *
from keystone import *
import pefile

#print '%x'%(crashStruct['EIP'])
#print crashStruct

## Address in memory where we want to overwrite. So that we can actually reach the shellcode.
## This is not really the target address. Still working on that one.
 crashStruct = crashStruct.FaultingIP
 crashStruct =  crashStruct & 0xffffffff
 crashAddress = 0x0040a000 + crashStruct
 #print '%x'%(crashAddress)
 # Now we want to add some shellcode so that the application calls shellcode
 # We want to go from here to a shellcode (must be in a shellcode)
 # I also want to be able to bypass the eax_stack_pivot workspace setup by John Lambert
 #
 ## Shellcode
 # Find out where the payload starts in memory. The function virtualAlloc will allocate memory on a 32
 # bit boundary, this is not the case for a shellcode. The shellcode image will
