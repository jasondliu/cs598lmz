import threading
# Test threading daemon status
t = threading.Thread(target=thread_function, args=(1,))
print(t.isDaemon())
t.start()
t.join()
print(t.isDaemon())

thread_list = []
for i in range(10):
    t = threading.Thread(target=thread_function, args=(1,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

# Test threading daemon status
t = threading.Thread(target=thread_function, args=(1,), daemon=True)
print(t.isDaemon())
t.start()
t.join()
print(t.isDaemon())

thread_list = []
for i in range(10):
    t = threading.Thread(target=thread_function, args=(1,), daemon=True)
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:

