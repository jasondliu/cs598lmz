import ctypes
ctypes.windll.msvcrt.SetConsoleTitleA("Campbell v0.1") # Sets the console title to 'Campbell v0.1'

host = input("Enter Host: ")
port = input("Enter Port: ")

s = socket.socket()
s.bind((host, int(port)))
s.listen(1)

while True:
    print("Waiting for user connection...")
    sc, add = s.accept()
    print("Connection found!")
    print("Client's IP address is", add[0])
    print("Client's Port is", add[1])
    print("Incoming Message: ", str(sc.recv(1024), "utf-8"))  # Receives and prints the message from the client
    sc.send(bytes("Hello from the server!", "utf-8"))  # Sends a message back to the client
    sc.close()
