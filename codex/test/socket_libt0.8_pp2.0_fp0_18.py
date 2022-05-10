import socket
import sys

def Main():
    
    host = '127.0.0.1'
    port = 5000

    servername = raw_input('Enter the name of the server file: ')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Socket creation error: ' + str(msg[0]))
        sys.exit()

    s.connect((host, port))

    filename = s.recv(1024)
    filesize = s.recv(1024)
    filesize = int(filesize)
    print('Server wants to send ' + filename)
    print('File size is ' + str(filesize) + ' bytes')

    while True:
        choice = raw_input('Do you want to accept this file? (Y/N): ')

        if choice == 'Y':
            print('OK!')
            s.send("OK")

