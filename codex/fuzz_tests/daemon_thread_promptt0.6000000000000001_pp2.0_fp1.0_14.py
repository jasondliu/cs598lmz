import threading
# Test threading daemon

def counter(count):
    while True:
        sleep(1)
        print("[%s] => %s" % (threading.currentThread().getName(), count))
        count += 1

for i in range(10):
    t = threading.Thread(target=counter, args=(i,))
    t.setDaemon(True)
    t.start()

print("Waiting for all threads to complete")
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

print("All threads complete")

# Waiting for all threads to complete
# [Thread-1] => 0
# [Thread-2] => 1
# [Thread-3] => 2
# [Thread-4] => 3
# [Thread-5] => 4
# [Thread-6] => 5
# [Thread-7] => 6
# [Thread-8] => 7
# [Thread-9] => 8
# [Thread-10] => 9
# All threads complete
