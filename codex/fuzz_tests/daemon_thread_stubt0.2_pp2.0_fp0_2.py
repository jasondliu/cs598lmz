import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.flush()
    sys.stderr.write('\n')
    sys.stderr.flush()

threading.Thread(target=run).start()

# vim: et sw=4 sts=4
