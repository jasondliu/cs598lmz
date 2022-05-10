import sys, threading

def run():
    sys.stdout.write('\x1b]2;@{}\x07'.format(sys.argv[1]))
    threading.Thread(target=run).start()
run()
