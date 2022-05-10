import sys, threading

def run():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print("thread running")
        time.sleep(1)

def test():
    t = threading.Thread(target=run)
    t.start()
    time.sleep(5)
    t.do_run = False
    t.join()
    print("thread stopped")

if __name__ == "__main__":
    test()
