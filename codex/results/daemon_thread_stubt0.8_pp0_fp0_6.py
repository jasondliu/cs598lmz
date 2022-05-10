import sys, threading

def run():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((sys.argv[1], int(sys.argv[2])))
	server.listen(1)
	print("Server listening...")
	conn, addr = server.accept()
	print("Client connected...")
	
	threading.Thread(target=sendData, args=(conn,)).start()
	threading.Thread(target=receiveData, args=(conn,)).start()
	
def sendData(conn):
	while True:
		conn.send(str.encode(input("Enter Text: ")))
		

def receiveData(conn):
	while True:
		print("Data Received: ", str(conn.recv(1024), "utf-8"))

if __name__ == "__main__":
	run()
