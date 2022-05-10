import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        while True:
            print('Running')
            time.sleep(1)
            
MyThread()

while True:
    print('Main thread')
    time.sleep(1)

# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
# Main thread
#
