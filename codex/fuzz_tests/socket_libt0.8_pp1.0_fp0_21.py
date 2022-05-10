import socket

host = socket.gethostname()
port = 56789

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(1)

while True:
    conn, addr = serversocket.accept()
    print("Connection from: " + str(addr))
    data = conn.recv(1024)
    print("Received from Client: " + str(data.decode("utf-8")))
    message = str(data.decode("utf-8")).upper()
    print("Sending to Client: " + message)
    conn.send(message.encode("utf-8"))
    conn.close()
