import threading
# Test threading daemon mode
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()

# Test threading.Thread
class MyThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num

	def run(self):
		print('Running on number: %s' % self.num)
		time.sleep(3)

if __name__ == '__main__':

