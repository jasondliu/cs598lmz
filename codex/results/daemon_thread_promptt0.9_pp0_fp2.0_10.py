import threading
# Test threading daemon

# def worker():
#     print("I'm a thred")
#     threadID = threading.current_thread()
#     print("thread id a: %s" %threadID)
#     t = threading.current_thread()
#     print("thread id b: %s" % t)
#
# new_t = threading.Thread(target=worker)
# new_t.start()

# threading attempt 2

def worker(num):
    print("Thred %s" %num)
    return

threads = []
for i in range(6):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()
