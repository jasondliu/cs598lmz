import threading
# Test threading daemon
def test_daemon():
	while True:
		print("This is a test daemon")
		time.sleep(1)

t = threading.Thread(target=test_daemon)
t.setDaemon(True)
t.start()

while True:
	print("This is the main thread")
	time.sleep(1)
