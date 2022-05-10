import sys, threading

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    while True:
        data = s.recv(1024)
        if data == "close":
            break
        print data
    s.close()

if __name__ == "__main__":
    try:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
    except:
        print "Usage: python client.py <server IP> <server port>"
        sys.exit()
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        data = raw_input()
        if data == "close":
            break
        data = data + "\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(data)
        s.close()
