import sys, threading

def run():
    print("Thread %s started" % threading.current_thread().name)
    while True:
        pass
    print("Thread %s finished" % threading.current_thread().name)

if __name__ == "__main__":
    print("Thread %s started" % threading.current_thread().name)
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
    print("Thread %s finished" % threading.current_thread().name)
