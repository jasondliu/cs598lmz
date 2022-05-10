import threading
# Test threading daemon

# test
class test(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)

	def run(self):
		i = 0
		while True:
			print "Run test, i = " + str(i)
			i = i + 1
			time.sleep(1)

# main
if __name__ == "__main__":
	# start test thread
	t = test()
	t.start()

	i = 0
	while True:
		print "Run main, i = " + str(i)
		i = i + 1
		time.sleep(1)
