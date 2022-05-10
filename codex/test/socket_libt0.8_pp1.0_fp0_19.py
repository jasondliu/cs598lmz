import socket #Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.9'
port = 12346
s.connect((host, port))
while True:
    filename = raw_input('Filename? -> ')
    if filename != 'q':
        s.send(filename)
    else:
        break
    data = s.recv(1024)
    if data[:6] == 'EXISTS':
        filesize = long(data[6:])
        message = raw_input('File exists, '+str(filesize)+'Bytes, download? (Y/N)? -> ')
        if message == 'Y':
            s.send('OK')
            f = open('new'+filename, 'wb')
            data = s.recv(1024)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = s.recv(1024)
                totalRecv += len(data)
