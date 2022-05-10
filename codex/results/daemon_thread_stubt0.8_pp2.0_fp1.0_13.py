import sys, threading

def run():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect((HOST, PORT))
    data = 'Hello'
    while True:
        # tcpCliSock.send(('%s\r\n' % data).encode())
        tcpCliSock.send(data.encode())
        if data == 'quit': break
        data = input()

    tcpCliSock.close()
    print('end')
    sys.exit()

if __name__ == '__main__':
    thread1 = threading.Thread(target=run)
    thread1.start()
