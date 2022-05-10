from bz2 import BZ2Decompressor
BZ2Decompressor

with ss.create_server((ss.gethostname(), 3009), ss.BaseRequestHandler) as s:
    sock, address = s.accept()
    bytes_received = 0
    while True:
        msg = sock.recv(1024)
        #print(msg)
        if not msg:
            break
        bytes_received += len(msg)
        print(len(msg))

        data = pickle.loads(msg)
        print(data)

    print('No more data from', address)
