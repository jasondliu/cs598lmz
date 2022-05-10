import threading
# Test threading daemon
def test_threading_daemon():
	def daemon():
		print("Start daemon")
		time.sleep(1)
		print("End daemon")
	d = threading.Thread(name='daemon', target=daemon)
	d.setDaemon(True)
	d.start()
	d.join()
	print("End main")

# Test threading
def test_threading():
	def worker():
		print("Start worker")
		time.sleep(1)
		print("End worker")
	w = threading.Thread(name='worker', target=worker)
	w.start()
	w.join()
	print("End main")

if __name__ == '__main__':
	test_threading()
