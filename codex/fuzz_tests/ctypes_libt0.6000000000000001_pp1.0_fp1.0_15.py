import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PyChatRoom")

while True:
    data = s.recv(1024)
    print(data.decode())
    if not data:
        sys.exit()
    cmd = input()
    if cmd == "exit":
        s.sendall(cmd.encode())
        s.close()
        break
    s.sendall(cmd.encode())
