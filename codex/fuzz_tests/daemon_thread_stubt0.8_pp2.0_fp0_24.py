import sys, threading

def run():
    print("aaa")
    sys.stdout.flush()
    time.sleep(0.5)

def run2():
    print("bbb")

def run3():
    print("ccc")

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread2 = threading.Thread(target=run2)
    thread3 = threading.Thread(target=run3)
    thread.start()
    thread2.start()
    thread3.start()
