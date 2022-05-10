import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect('test.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#conn.close()

# Test ctypes
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print 'pid:', libc.getpid()

# Test threading
#def worker():
#    print 'Worker'
#    return
#
#threads = []
#for i in range(5):
#    t = threading.Thread(target=worker)
#    threads.append(t)
#    t.start()

# Test os
#print os.getpid()

# Test sys
#print sys.argv

# Test time
#print time.time()

# Test random
#print
