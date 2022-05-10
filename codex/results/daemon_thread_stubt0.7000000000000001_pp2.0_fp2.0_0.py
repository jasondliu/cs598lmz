import sys, threading

def run():
	threading.Thread(target = lambda: ser.read(ser.inWaiting())).start()
	while True:
		try:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect((ip, port))
			client.send(ser.readline())
			client.close()
		except Exception:
			print("[*] Error occured")
			sys.exit(1)

if __name__ == "__main__":
	ip = "192.168.1.3"
	port = 7777

	ser = serial.Serial("/dev/ttyACM0", 9600)
	run()
