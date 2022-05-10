import threading
# Test threading daemon
"""
class KnobThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.value = False
        self.daemon = True
    def run(self):
        while True:
            if self.value:
                print("Hello World")
                self.value = False
            time.sleep(0.1)

knobThread = KnobThread()
knobThread.start()

run = True
while run:
    data = raw_input("Knob Thread: ")
    if data == "exit":
        run = False
    elif data == "hello":
        knobThread.value = True

knobThread.join()
"""

#Command line interface
class CommandLineInterface(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.run = True
        self.daemon = True
        self.commands = {"q": self.exit,
                         "1": self.zero,
                         "2": self
