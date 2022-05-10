import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print("Hello")
