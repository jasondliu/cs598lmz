import sys, threading

def run():
    print("Thread %s started" % threading.current_thread().name)
    for i in range(5):
        print("Thread %s is running" % threading.current_thread().name)
    print("Thread %s ended" % threading.current_thread().name)

if __name__ == "__main__":
    print("Thread %s started" % threading.current_thread().name)
    t = threading.Thread(target=run, name="MyThread")
    t.start()
    t.join()
    print("Thread %s ended" % threading.current_thread().name)
