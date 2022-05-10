import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


def main():
	if len(sys.argv) != 4:
		print('usage: {0} <image> <outfile> <path_to_libc>')
		exit(1)
		
	image = sys.argv[1]
	outfile = sys.argv[2]
	libc = sys.argv[3]
	
	f = open(outfile, 'wb')
	
	# read in libc
	libc = open(libc, 'rb').read()
	
	# read in the image
	image = open(image, 'rb').read()
	
	# write out the image
	f.write(image)
	
	# write out the libc
	f.write(libc)
	
	# write out a null byte
	f.write(b'\x00')
	
	# write out the address of the first byte of the libc to call
	f.write(struct.pack('<Q', 0x400000))
	
	# write out the address
