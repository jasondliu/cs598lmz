import sys, threading

def run():
    global tcpsock, tcpconnected, host
    print "[*] Connected to: " + host + ":" + str(port)

    while True:
        r, w, e = select.select([sys.stdin, tcpsock], [], [])
        if tcpsock in r:
                data = tcpsock.recv(1024)
                if len(data) == 0:
                    print "\r[*] Disconnected"
                    break
                else:
                    sys.stdout.write(data)

        if sys.stdin in r:
                data = unicode(sys.stdin.readline())
                tcpsock.sendall(data)

    sys.exit(0)

def main():
    
    global tcpsock, host, port
    host = raw_input("[*] Enter target host: ")
    port = int(raw_input("[*] Enter target port: "))

    try:
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.sets
