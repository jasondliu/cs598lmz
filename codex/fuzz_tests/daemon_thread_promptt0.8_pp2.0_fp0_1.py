import threading
# Test threading daemon
class MyDaemon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            #print "I'm alive!"
            time.sleep(1)

def main():
	print "In Main: making daemon"
	d = MyDaemon()
	print "In Main: starting daemon"
	d.start()
	print "In Main: waiting"
	time.sleep(5)
	print "In Main: waiting some more"
	time.sleep(5)
	print "In Main: exiting"

if __name__ == "__main__":
    main()
