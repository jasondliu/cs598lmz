import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[33m')).start()

def exit():
	global longpress
	if longpress:
		sys.exit()
	else:
		print('Action aborted by user.')

def is_hex(s):
	try:
		int(s, 16)
		return True
	except ValueError:
		return False

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def text_to_hex(s):
	return ''.join(str(hex(ord(c))[2:]) for c in s)

def text_to_opcode(s):
	return ''.join(str(hex(ord(c))[2:]).zfill(2) for c in s)

def hex_to_text(s):
	return ''.join(chr(int(s[i:i + 2], 16)) for i in range(0, len(s), 2))

def
