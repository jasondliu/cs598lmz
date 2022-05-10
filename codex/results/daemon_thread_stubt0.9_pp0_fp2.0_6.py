import sys, threading

def run():
	global sock
	global msg
	global type
	global ver
	global opcode
	global length
	global RFIFO
	global TFIFO

	print("Interactive Mode")
	RFIFO = ""
	TFIFO = ""
	sock = createConnection("127.0.0.1", 27960)
	
	while True:
		inData = input("send: ")
		if len(inData) == 0:
			continue
		if inData == "exit":
			break
		
		if inData == "ping":
			TFIFO = TFIFO + struct.pack("<BB", 0x12, 0x00)
			TFIFO = TFIFO + struct.pack("<B", 0x00)
			TFIFO = TFIFO + struct.pack("<B", 0x00)
			TFIFO = TFIFO + struct.pack("<I", 0x01)
			TFIFO = TFIFO + struct.pack("<I
