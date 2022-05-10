import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("EasySalty v.1.0")

def smartprint(msg, hardreturn = False):
	if hardreturn:
		subprocess.call('cls',shell=True)
	print(msg)
	time.sleep(0.2)

def bytetodec(bytd):
	i = int.from_bytes(bytd,"big")
	return i
def dectobyt(de):
	return de.to_bytes((de.bit_length() + 7) // 8, 'big')

def add0(instring,length=2):
	# takes a string and adds trailing zeros.
	# optional argument length specifies how many zeros are to be appended.
	# if the input string starts with "0x", the zeros will be added before "x".
	# if the input string doesn't start with "0x", the zeros will be added at the end
	# of the string.
	while len(instring)<length:
		if instring.startswith("0x"
