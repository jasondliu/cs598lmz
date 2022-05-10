import ctypes
ctypes.windll.Kernel32.SetConsoleTitleA("Client")


def Connect():
    global ClientSocket

    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClientSocket.connect(ClientAdd)
    print("Connected")

def RecieveMsg():
    while True:
        try:
            RecievedMsg = ClientSocket.recv(1024).decode()
            print("\n" + RecievedMsg)
            RecieveMsg()

        except (RuntimeError, TypeError, NameError, ValueError):
            print("Disconnected")
            time.sleep(1)
            sys.exit()


def SendMsg():
    while True:
        if b'\x01' in ClientSocket.recv(1024):
            print("\nConnection Lost")
            time.sleep(1)
            sys.exit()

        try:
            Message = input(Fore.GREEN+"Client: ")
            ClientSocket.send(Message.encode())

        except (RuntimeError, TypeError, NameError, ValueError):
            print
