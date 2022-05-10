import sys, threading

def run():
    while True:
        sys.stdout.write("\r{}".format(datetime.datetime.now().time()))
        sys.stdout.flush()
        time.sleep(0.1)

threading.Thread(target=run).start()
</code>

