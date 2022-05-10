import sys, threading
threading.Thread(target=lambda:sock.listen(1)).start()
while True:
    conn, addr = sock.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
    conn.close()
    print('client disconnected')
