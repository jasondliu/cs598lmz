import sys, threading

def run():
    print("thread running")

t = threading.Thread(target=run)
t.start()

while True:
    print("thread is alive:", t.is_alive())
    time.sleep(0.5)
    if not t.is_alive():
        sys.exit(0)
