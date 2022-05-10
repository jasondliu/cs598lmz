import sys, threading

def run():
    sys.stdout.write('start running')
    time.sleep(0.1)
    sys.stdout.write('finish running')

threading.Thread(target=run).start()
