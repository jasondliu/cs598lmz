import sys, threading

def run():
    while True:
        try:
            connection, address = sock.accept()
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                if buf == '1':
                    connection.send('welcome to server!')
                else:
                    connection.send('please go out!')
            except socket.timeout:
                print 'time out'
            connection.close()
        except:
            print 'error'

if __name__ == '__main__':
    host = ''
    port = 12345
    bufsize = 1024
    addr = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    for i in range(3):
        t = threading.Thread(target=run)
        t.start()
    sock.close()
