import sys, threading

def run():
    f = open(sys.argv[1], "rb")
    data = f.read()
    f.close()
    sys.stdout.write(data)

thread = threading.Thread(target = run)
thread.daemon = True
thread.start()

def target():
    for i in range(10):
        print(i, threading.current_thread().name)
        time.sleep(1)

threading.Thread(target=target, args=(), kwargs={}, daemon=False).start()

for i in range(5):
    print(i, threading.current_thread().name)
    time.sleep(1)
