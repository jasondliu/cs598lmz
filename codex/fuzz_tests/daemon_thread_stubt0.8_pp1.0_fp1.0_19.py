import sys, threading

def run():
    while True:
        while True:
            start = time.time()
            try:
                conn, addr = soc.accept()
            except socket.error as msg:
                print(msg)
                continue
            break
        conn.settimeout(5.0)
        data = conn.recv(1024)
        conn.settimeout(None)
        if data == "":
            continue
        print(data)
        with open(data, "rb") as file:
            data = file.read()
            conn.send(data)

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("Usage: server.py [ip] [port]")
        exit(1)
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((sys.argv[1], int(sys.argv[2])))
    soc.listen(1)
    threading.Thread(target = run).start()
