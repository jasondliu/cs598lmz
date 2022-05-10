import sys, threading

def run():
    while True:
        print("thread %s is running..." % threading.current_thread().name)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

t.join()

print("thread %s ended." % threading.current_thread().name)
