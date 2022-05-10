import sys, threading

def run():
    print("start")
    sys.stdout.flush()
    for i in range(10):
        print(i)
        sys.stdout.flush()
        time.sleep(1)
    print("end")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

