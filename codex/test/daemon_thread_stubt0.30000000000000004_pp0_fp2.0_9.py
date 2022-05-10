import sys, threading

def run():
    try:
        while True:
            print("Hello World")
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

thread = threading.Thread(target=run)
thread.start()
