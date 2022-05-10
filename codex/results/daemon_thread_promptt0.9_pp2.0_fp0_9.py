import threading
# Test threading daemon and non-deamon thread

def worker(num, job_list):
    for job in job_list:
        print("Worker %d: %s" % (num, job))
        time.sleep(1)

jobs = ["one", "two", "three", "four"]

w1 = threading.Thread(target=worker, name="worker1", args=(1, jobs))
w1.setDaemon(True)    # !!!
w2 = threading.Thread(target=worker, name="worker2", args=(2, jobs))

w2.start()
w1.start()

print("started")
# Sleep to allow threads finish
time.sleep(5)
print("finish")
