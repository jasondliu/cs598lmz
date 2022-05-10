import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class WinLircSender:

    def __init__(self):
        self.host = "localhost"
        self.port = 8765
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_command(self, remote_control_name, remote_control_command):
        self.sock.send(remote_control_name + " " + remote_control_command + "\n")
        self.sock.recv(1024)
        print(remote_control_name + " " + remote_control_command)

    def close(self):
        self.sock.close()

def main():
    WinLircSender().send_command("Toshiba", "KEY_POWER")

main()
