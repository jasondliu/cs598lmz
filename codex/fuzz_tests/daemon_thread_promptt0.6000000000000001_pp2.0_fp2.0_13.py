import threading
# Test threading daemon
def test_function(a,b):
	print "in test_function"
	print a + b
	time.sleep(2)
	print "end test_function"

def main():
	print "in main"
	a = threading.Thread(target=test_function, args=('test', 'test2'))
	a.daemon = True
	a.start()
	print "end main"

if __name__ == '__main__':
	main()
