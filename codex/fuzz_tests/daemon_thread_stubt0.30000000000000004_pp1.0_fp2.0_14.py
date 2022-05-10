import sys, threading

def run():
    for i in range(3):
        print("thread %d" % i)
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("main thread")
