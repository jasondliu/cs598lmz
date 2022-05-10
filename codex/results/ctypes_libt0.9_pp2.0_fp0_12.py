import ctypes
ctypes.SoapCall.argtypes = [ctypes.py_object]

# really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long comment


# control characters and printable characters for 0000 2fff
#
# idx character
# 0 none
# 1,2 end of document
# 3,4 end of line
# 5 u00c
# 6 character padding
# 7 horizontal tab
# 8 direct cursor movement
# 9 back space
# 9 u00b
# a lf
# 10,c cr
# b,b u00d
# c,c u200d
printable = 0

while True:

	b = f.read(1)

	if len(b) == 0:
		break

	b = ord(b)

	printable = printable | (b >= 0x20 and b < 0x80)

	print table.readword(idx)
