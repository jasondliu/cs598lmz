import sys, threading

def run():
    while True:
        try:
            print("trying")
            time.sleep(1)
        except KeyboardInterrupt:
            print("exiting")
            sys.exit()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    try:
        print("main")
        time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        sys.exit()
</code>

