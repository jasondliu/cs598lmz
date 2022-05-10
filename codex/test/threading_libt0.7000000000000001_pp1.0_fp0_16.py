import threading
threading.Thread(target=client, args=(sock,)).start()

sock.send(b"#hello\n")

def ping(sock):
    while True:
        sock.send(b"#ping\n")
        time.sleep(10)
threading.Thread(target=ping, args=(sock,)).start()

while True:
    message = input("> ")
    if message[0] == "/":
        if message == "/quit":
            sock.send(b"#quit\n")
            break
        elif message == "/ping":
            sock.send(b"#ping\n")
        elif message == "/exit":
            break
        elif message[:6] == "/nick ":
            sock.send(bytes(message, "utf-8"))
        else:
            print("Unknown command: " + message)
        continue
    sock.send(bytes(message, "utf-8"))
