import threading
# Test threading daemon
def worker():
    print("Worker")
    while True:
        time.sleep(0.5)
        print("Worker")

t = threading.Thread(target=worker)
t.daemon = True
t.start()
t.join()

# Test threading
# thread_list = []
# for i in range(5):
#     thread = threading.Thread(target=worker)
#     thread.start()
#     thread_list.append(thread)
#
# for thread in thread_list:
#     thread.join()
