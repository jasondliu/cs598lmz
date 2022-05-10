import sys, threading

def run():
    try:
        print("[*] Connection from " + str(addr[0]) + ':' + str(addr[1]))
        while True:
            data = conn.recv(2048)
            if not data:
                break
            print("[*] Received: " + data.decode('utf-8'))
            conn.sendall(data)
        print("[*] Connection closed")
    except:
        print("[!] Error")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <host> <port>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)

    print("[*] Listening on " + host + '
