import sys, threading

def run():
    sys.stdout.write("Starting ")
    sys.stdout.flush()
    for i in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("End")
t = threading.Thread(target=run)
t.start()
