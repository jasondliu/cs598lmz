import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect('/home/david/Desktop/test.db')
#print "Opened database successfully";
#conn.close()

# Test ctypes
#lib = ctypes.CDLL(ctypes.util.find_library('c'))
#lib.printf(b"Hello, World\n")

# Test threading
#def thread_function(name):
#    print "Thread %s: starting" % name
#    time.sleep(2)
#    print "Thread %s: finishing" % name
#
#if __name__ == "__main__":
#    x = threading.Thread(target=thread_function, args=(1,))
#    y = threading.Thread(target=thread_function, args=(2,))
#    x.start()
#    y.start()
#    x.join()
#    y.join()
#    print "Done"

# Test sqlite3 threading
#conn = sqlite3.connect('/home/david/Desktop/test.db')
#print "
