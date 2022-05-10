import socket

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s2.bind(("127.0.0.1", 5000))
s2.listen(5)

while 1:
    s, a = s2.accept()

    data = s.recv(8)
    print("data:", data)
    print("hex data: ", ' '.join(hex(b) for b in data))
    print("addr:", a)

    size = int.from_bytes(data[0:4], byteorder='little')

    while len(data) != size:
        data += s.recv(4096)
        data = bytearray(data)

    print("final:", len(data))
    s.close()
