import codecs
# Test codecs.register_error('euc2cp932')

import java

print 'py:', sys.version
print 'jp:', java.lang.System.getProperty("java.version")

# a test.
import collections
import threading

import re
print bool(re.match("^1\.0\.[123]\.0_20$", sys.version))
print bool(re.match("^1\.6\.0_20$", java.lang.System.getProperty("java.version")))

lock = threading.Lock()

def f():
    lock.acquire()
    print "got lock in thread"
    jpyutil.execInThreadWithCleanup(f2, lock)
    print "DONE", threading.current_thread()
    lock.release()

def f2():
    print "thread-2", threading.current_thread()
    
print "main", threading.current_thread()
jpyutil.execInNewThread(f)
print "main 2", threading.current_thread()
