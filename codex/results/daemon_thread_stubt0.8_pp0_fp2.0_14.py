import sys, threading

def run():
    print "Running..."

class InputThread(threading.Thread):
    def run(self):
        global running
        raw_input()
        running = False

running = True
threading.Thread(target=run).start()
InputThread().start()
while running:
    time.sleep(0.1)
</code>

