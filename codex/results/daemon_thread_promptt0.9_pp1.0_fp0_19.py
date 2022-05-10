import threading
# Test threading daemon mode
# When main thread exit, all secondary threads will be terminated 
# The output should be "111helloworld222"
# The threads should not be blocked and wait for the main thread
# When main thread exit, all secondary threads will be terminated as daemon
# Then, print "222" in second thread will not be interrupted

def hello():
	while True:
		sys.stdout.write('111\n')
		sys.stdout.write('helloworld\n')

t = threading.Thread(target=hello, daemon=True)
t.start()

sys.stdout.write('222\n')
sys.stdout.write('2222\n')
