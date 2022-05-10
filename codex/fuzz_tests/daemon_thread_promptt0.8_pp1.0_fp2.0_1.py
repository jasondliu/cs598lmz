import threading
# Test threading daemon

def test():
	print "Test"
	time.sleep(10)
	print "Test"

if __name__ == '__main__':
	t = threading.Thread(target=test)
	t.setDaemon(True)
	t.start()
	t.join()
