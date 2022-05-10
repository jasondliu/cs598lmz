import threading
# Test threading daemon

def test_thread(i,d):
    print(i)
    time.sleep(d)
    print(i)

print("Start")
thread_list=[]
for i in range(1,20):
    s=threading.Thread(target=test_thread,args=(i,2))
    thread_list.append(s)
    s.setDaemon(True)
    s.start()

print("End")

print(threading.enumerate())
print(threading.active_count())



time.sleep(5)

print("End")
time.sleep(1)
print(threading.enumerate())
print(threading.active_count())
