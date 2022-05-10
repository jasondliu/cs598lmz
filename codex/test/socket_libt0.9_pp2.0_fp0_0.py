import socket
import threading as th
import os as os


def fun(client):
    client_bytes = client.recv(65536)
    client_str = client_bytes.decode()
    try:
        command = client_str.split(' ')[0]
        filename = client_str.split(' ')[2]
    except IndexError:
        client.close()
        print(f'[-] error command or filename')
        return
    path = os.path.join(os.getcwd(), 'FtService', filename)
    print(f'[+] client {client.getpeername()} :request: sendfile')
    print(f'[+] path : {path}')
    if command != 'GET':
        client.close()
        print(f'[-] error command')
        return
    print(f'[+] processing')
    if os.path.isfile(path):
        print(f'[*] Filename : {filename}')
        print(f'[+] sendfile')
