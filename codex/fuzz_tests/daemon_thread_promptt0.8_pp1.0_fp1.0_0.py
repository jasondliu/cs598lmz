import threading
# Test threading daemon mode
def func(name):
    print("hello",name)
    time.sleep(1)
    print("finish")
for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.setDaemon(True)
    t.start()

# Test threading Lock
num = 0
def run_thread(n):
    global num
    lock.acquire()
    temp = num
    time.sleep(0.01)
    num = temp+1
    lock.release()

lock = threading.Lock()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run_thread,args=[i,])
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()

print("all thread has finish")
print("num:%s"
