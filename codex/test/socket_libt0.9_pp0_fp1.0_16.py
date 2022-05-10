import socket
import threading

screenName = "home"
host = "192.168.4.1"
port = 23

def recv_msg(frame):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.bind((host, port))
    skt.listen(1)
    while True:
        try:
            client, addr = skt.accept()
            msg = client.recv(1024).decode()
            frame.updateData(msg)
        except:
            skt.close()
            os.system("kill -9 `pgrep -f 'python3 recv_msg.py'`")
            sys.exit(1)


if __name__ == "__main__":
    module = importlib.import_module(screenName)
    frame = module.init()
    thread = threading.Thread(target=recv_msg, args=(frame,))
    thread.start()
    frame.show()
