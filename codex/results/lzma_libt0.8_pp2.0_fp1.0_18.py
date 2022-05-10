import lzma
lzma.decompress(compressed_file)

destroy_compressed_file()

if ERROR_DETECTING_COMPRESSION_FUNCTION == True:
	for i in range(0, len(uncompressed_file), 1):
		if uncompressed_file[i] != new_file[i]:
			print('Error at byte %s' % str(i))
	print('Error detected')
else:
	print('compression function passed')


def destroy_new_file():
	global new_file
	new_file = []
	for i in range(0, len(new_file), 1):
		new_file[i] = randint(0, 255)


new_file = []

destroy_new_file()



decompression_function(uncompressed_file, new_file)

destroy_compressed_file()

if ERROR_DETECTING_DECOMPRESSION_FUNCTION == True:
	for i in range(0, len(uncompressed_file), 1):
		
