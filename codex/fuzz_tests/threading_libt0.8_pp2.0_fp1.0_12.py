import threading
threading.stack_size(5242880)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))

while True:
    msg = input("Enter Message: ")
    messages = msg.split(" ")
    if len(messages) == 2:
        s.sendall(bytes(msg, "utf8"))
    else:
        print("Communication Error: Invalid number of arguments!")

print("The end!")
