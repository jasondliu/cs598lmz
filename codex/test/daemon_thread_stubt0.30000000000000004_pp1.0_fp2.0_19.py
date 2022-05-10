import sys, threading

def run():
    while True:
        print("Hello from Python!")
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()
