import sys, threading

def run():
    main()

def main():
    host = 'localhost'
    port = 9999
    errcount = 0
    errcount_should = 10000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to %s port %s' % (host, port))
    sock.connect((host, port))

    while True:
        msg = 'This is the message.  It will be repeated.'
        print('sending "%s"' % msg)
        sock.sendall(msg.encode('utf-8'))
        errcount += 1
        if errcount > errcount_should:
            break
        time.sleep(0.001)

    print('closing socket')
    sock.close()

if __name__ == '__main__':
    client_thread = threading.Thread(name='client', target=run)
    client_thread.start()
