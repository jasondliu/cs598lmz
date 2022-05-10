import sys, threading

def run():
    while True:
        sys.stdout.write("\r" + str(datetime.datetime.now()))
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()
</code>

