import threading
# Test threading daemon
def threading_func(a, b, c):
     print("a:", a, "b:", b, "c:", c)
t = threading.Thread(target=threading_func, args = (2, 3, 4), daemon=True)
t.start()
t.isDaemon()
print("asd")




import threading
import time
from queue import Queue
import threading

q = Queue()  
for i in range(8):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()


for i in range(20):
    q.put(("clog -x .* OR .*http.* OR .*phoenix.* OR .*modelcache.jsp.* -f /logs/localhost_access_log.{date}.txt.gz".format(date=i+16), "tmp_log{date}_jsp_all.txt".format(date=i+16)))

q.join()       # block until all tasks are done
