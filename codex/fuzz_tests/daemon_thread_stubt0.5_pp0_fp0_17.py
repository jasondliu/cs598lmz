import sys, threading

def run():
    while True:
        sys.stdout.write('\r{}'.format(datetime.datetime.now()))
        sys.stdout.flush()

threading.Thread(target=run).start()
</code>

