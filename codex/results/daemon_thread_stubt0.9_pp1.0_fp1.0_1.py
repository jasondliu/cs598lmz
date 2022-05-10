import sys, threading

def run():
    global sockCli
    while True:
        try:
            msg = input('> ')
            sockCli.send(msg.encode())
            if msg == 'exit':
                print('[INFO] Exit client...')
                sockCli.close()
                break
        except:
            continue

host = 'localhost'
port = 8080
sockCli = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
sockCli.connect((host, port))
t = threading.Thread(target=run)
t.start()
while True:
    try:
        msg = sockCli.recv(1024)
        print(msg.decode())
    except:
        continue
