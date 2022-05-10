import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)

s.bind(("your ip address here",10000))

while True: 
    data = s.recv(1024)
    print data, type(data)
</code>

