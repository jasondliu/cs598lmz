import sys, threading

def run():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 1337))
        sock.send('/home/airwarn/find')
        data = sock.recv(1024)
        sock.close()
        print data
    except Exception:
        # Error out, something has gone wrong
        sys.stdout.write('.')
        sys.stdout.flush()
        return


for i in xrange(256):
    for j in xrange(256):
        for k in xrange(256):
            for l in xrange(256):
                running = True
                if k == 0:
                    # We're only attempting to ping
                    # 192.168.1.0/24, the broadcast
                    # address, and 192.168.1.255
                    continue
                if k == 8:
                    if l > 0:
                        break
                if k == 255:
                    if l != 255:
                        continue
                sys.stdout.write("Trying IP
