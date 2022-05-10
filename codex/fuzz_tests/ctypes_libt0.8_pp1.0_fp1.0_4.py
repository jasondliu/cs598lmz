import ctypes
ctypes.windll.user32.MessageBoxA(0, "listener has been started", "listener", 1)

s = socket()
s.bind(('', 9999))
s.listen(1)

while True:
    try:
        conn, client = s.accept()
        while True:
            try:
                data = conn.recv(1024)
                msg = data.decode()
                conn.send(b'haha')
            except Exception as e:
                print(e)
                conn.close()
                break
    except Exception as e:
        print(e)
        s.close()
        break
