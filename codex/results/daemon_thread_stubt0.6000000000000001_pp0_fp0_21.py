import sys, threading

def run():
	if len(sys.argv) < 2:
		print("Usage : python %s <filename> <operation>" % sys.argv[0])
		sys.exit(1)
	
	file = sys.argv[1]
	op = sys.argv[2]
	
	if op == 'encrypt':
		encrypt(file)
	elif op == 'decrypt':
		decrypt(file)
	else:
		print("Invalid operation %s" % op)
		sys.exit(2)

def encrypt(file):
	with open(file, 'rb') as f:
		data = f.read()
		data = data.decode('utf-8')
		data = data.encode('utf-16le')
	
	with open(file, 'wb') as f:
		f.write(data)

def decrypt(file):
	with open(file, 'rb') as f:
		data = f.read()
		data = data.decode('utf-
