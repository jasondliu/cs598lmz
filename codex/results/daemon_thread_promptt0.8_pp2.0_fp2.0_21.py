import threading
# Test threading daemon
# https://docs.python.org/2/library/threading.html
# http://pymotw.com/2/threading/

def worker(num):
	"""thread worker function"""
	print 'Worker: worker %s' % num
	return

threads = []
for i in range(5):
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()
