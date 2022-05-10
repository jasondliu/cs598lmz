import sys, threading

def run():
    sys.stdout.write('thread running\n')

sys.stdout.write('starting\n')
threading.Thread(target=run).start()
sys.stdout.write('ending\n')
