import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("wamo")

ip = input("Enter IP: ")

if ip == "":
    ip = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(input("Enter Port: "))))
s.sendall(bytes(input("Enter Username: ") + "\n", "utf-8"))

t1 = threading.Thread(target=send_thread, args=(s,))
t2 = threading.Thread(target=recv_thread, args=(s,))

t1.start()
t2.start()

s.close()
</code>
If you need more code, I can try to provide it.
Thank you for your help!

