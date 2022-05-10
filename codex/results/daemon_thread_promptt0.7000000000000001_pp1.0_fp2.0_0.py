import threading
# Test threading daemon
class ReceiveThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.daemon = True
        self.start()
    def run(self):
        while True:
            try:
                x = receive()
                self.parent.receive_queue.put(x)
            except Exception as e:
                print("ReceiveThread Exception", e)
            time.sleep(0.1)

class TextDisplay(tkinter.Frame):
    def __init__(self, parent, receive_queue):
        tkinter.Frame.__init__(self, parent)
        self.text = tkinter.Text(self)
        self.vsb = tkinter.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("red", foreground="#ff0000")
        self.text.tag_configure("
