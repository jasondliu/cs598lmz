import sys, threading

def run():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8888))
    while True:
        try:
            data = s.recv(1024)
            if data:
                print("Received: " + data.decode("utf-8"))
        except:
            print("Connection closed")
            s.close()
            break

def send():
    global s
    while True:
        msg = input()
        s.send(msg.encode("utf-8"))

if __name__ == "__main__":
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=send)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
