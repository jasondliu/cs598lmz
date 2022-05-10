import sys, threading

def run():
    print("run")
    sys.stdout.flush()
    for i in range(1, 100):
        print(i)
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()
