import threading
threading.stack_size(1024*1024*1024)

def rec(ips, port, t):
    #print "receiving Packets"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ips, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
