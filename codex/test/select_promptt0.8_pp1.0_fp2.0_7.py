import select
# Test select.select()

def select_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 2. create a socket,   family = AF_INET,  type = SOCK_STREAM
    s.connect(('127.0.0.1', 3000))  # 3. connect to the server
    s.setblocking(False)

    rs = [s]
    ws = [s]
    xs = [s]

    while True:
        read_list, write_list, excep_list = select.select(rs, ws, xs, 1)

        for r in read_list:
            print('read from server...')
            print(s.recv(1024).decode('utf8'))

        for w in write_list:
            print('send to server...')
            w.send('Hello, World'.encode('utf8'))   # encode, translate string to binary string

        for x in excep_list:
            print('error, shut down socket')
