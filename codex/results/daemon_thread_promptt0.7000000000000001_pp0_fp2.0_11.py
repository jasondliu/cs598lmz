import threading
# Test threading daemon

# Main daemon class
class MyDaemon(threading.Thread):
    def run(self):
        while True:
            time.sleep(1)
            print "Daemon thread"

# Main thread class
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print "Main thread"

# Main function
def main():
    daemon = MyDaemon()
    daemon.daemon = True
    daemon.start()
    my_thread = MyThread()
    my_thread.start()


if __name__ == "__main__":
    main()
