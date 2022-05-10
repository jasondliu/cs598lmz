from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(my_data)



####################
# File Variables
####################

f = open(relative_path, "r")
f = open(os.path.join(dirname, filename), "r")
f.read(); f.readline(); f.read(n)
f.readlines() 	# gets all the lines in the file
for line in f:	# gets all lines in the file but does not have to save them to memory
	print(line)
f.write(string)		# writes the string to the file
f.seek(n)		# seek moves the current position for reading and writing to n, default is 0
f.tell()		# gets the current position
f.close()
f.flush()		# write everything in a buffer to a file
with open(file) as f:	# this file will be closed automatically
	f.read()
f = open(file, "r")
print(f.readline())
f.seek(0)
f.readline()
f.seek(0)
f.readlines()
