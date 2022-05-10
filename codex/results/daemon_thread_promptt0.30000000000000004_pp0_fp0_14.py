import threading
# Test threading daemon

class Threading_Daemon(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True

    def run(self):
        print("Starting " + self.name)
        while True:
            print("Running " + self.name)
            time.sleep(1)
        print("Exiting " + self.name)

def main():
    thread1 = Threading_Daemon("Thread-1")
    thread1.start()
    time.sleep(5)
    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
