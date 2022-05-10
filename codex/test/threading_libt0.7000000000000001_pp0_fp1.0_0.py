import threading
threading.stack_size(2**27)
thread = threading.Thread(target=urllib2.urlopen,
                          args=('http://www.python.org',))
thread.start()
