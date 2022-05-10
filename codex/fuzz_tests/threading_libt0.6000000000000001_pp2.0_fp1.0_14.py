import threading
threading.stack_size(1024*1024*1024)

def rec(ips, port, t):
    #print "receiving Packets"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ips, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        data = conn.recv(1024)
        if not data:
            break
        print "received data:", data
        conn.close()

def send(ips, port, t):
    #print "Sending packets"
    s = socket.socket()
    s.connect((ips, port))
    for i in range(t):
        print "Sending packet ", i
        s.send(str(i))
    s.close()

def main():
    ips = "127.0.0.1"
    port = 8888
    t = 1000000
    s = threading.Thread(target=send, args=(ips, port
