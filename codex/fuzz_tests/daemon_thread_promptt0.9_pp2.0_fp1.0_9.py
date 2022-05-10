import threading
# Test threading daemon thread
# t1 = threading.Thread(target=xxx, args=(), daemon = True)
# t1.start()
# t1.join()

class Threadp(threading.Thread):
    def __init__(self, name, id, ch, cm):
        super().__init__(daemon = True)
        self.name = name
        self.id = id
        self.ch = ch
        self.cm = cm

    def run(self):
        while True:
            number = self.ch.get(self.name)
            with self.cm:
                print(f"{self.name}{self.id} {number}")
                time.sleep(random.uniform(0.1, 3))

class WebChatServer:
    def __init__(self):
        self.cm = threading.Condition()
        for k in range(5):
            t1 = Threadp("chef ", k, ChatQueue(), self.cm)
            t1.start()
        threading.Thread(target=self.server_conn, daemon=True).
