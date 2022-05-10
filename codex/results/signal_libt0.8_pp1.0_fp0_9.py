import signal
signal.signal(signal.SIGINT, signal_handler)

ip_addr = "192.168.1.2"
listener = Listener(ip_addr)

print "Binding to local address and port", ip_addr + ":50007"
listener.bind((ip_addr, 50007))
listener.listen(5)

print "Server listening for incoming connections..."

while True:
    (conn, addr) = listener.accept()
    print "Received connection from:", addr
    data = conn.recv(1024)
    print "Received data:", data
    conn.send(data)
    conn.close()
