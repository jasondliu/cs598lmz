import threading
# Test threading daemon block

#t1 = threading.Thread(target=thread_test)
def thread_test():
  while (1):
    print("Thread: 1")
    time.sleep(1)

t1 = threading.Thread(target=thread_test)
t1.daemon = True
t1.start()

print("==========")

t2 = threading.Thread(target=thread_test)
#t2.daemon = True
t2.start()

print("==========")

t3 = threading.Thread(target=thread_test)
#t3.daemon = True
t3.start()

"""
print("==========")

t4 = threading.Thread(target=thread_test)
#t4.daemon = True
t4.start()
"""
