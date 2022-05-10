import selectors
from AIMLBot import AIMLBot


class Client:
    def __init__(self, addr):
        self.addr = addr
        self.sel = selectors.DefaultSelector()
        self.bot = AIMLBot()
        self.bot.learn("./chatbot/chatbot.aiml")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(self.addr)
        server.listen()
        print("listening on", self.addr)
        server.setblocking(False)
        self.sel.register(server, selectors.EVENT_READ, self.accept)

    def accept(self, sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print("accepted", conn, "from", addr)
