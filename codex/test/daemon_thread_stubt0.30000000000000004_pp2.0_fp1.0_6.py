import sys, threading

def run():
    for i in range(5):
        print("threading %s is running..." % threading.current_thread().name)
        time.sleep(1)
    print("threading %s is ended." % threading.current_thread().name)

print("threading %s is running..." % threading.current_thread().name)
t = threading.Thread(target=run, name="MyThread")
t.start()
t.join()
print("threading %s is ended." % threading.current_thread().name)
