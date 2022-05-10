import threading
# Test threading daemon
class thread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print self.name

def main():
    t = thread("Test")
    t.setDaemon(True)
    t.start()
    t.join()
    print "Main thread done"

if __name__ == "__main__":
    main()
