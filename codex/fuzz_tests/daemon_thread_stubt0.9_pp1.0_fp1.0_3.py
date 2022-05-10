import sys, threading

def run():
    serverPort = 12600
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
    while 1:
        threading.Thread(target=receiveClient, args = (serverSocket,)).start()


def receiveClient(serverSocket):
    connsoc, addr = serverSocket.accept()

    print("Connect", addr)

    input = "let it go"
    while input != "bye":
        input = input.replace("'", "`")
        input = input.replace("\"", "``")
        data = bytes(input, 'utf-8')
        connsoc.sendall(data)
        input = connsoc.recv(1024).decode()
        print("\t", input)

    connsoc.close()
    print("Closed", addr)

run()
