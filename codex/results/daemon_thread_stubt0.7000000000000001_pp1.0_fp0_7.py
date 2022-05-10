import sys, threading

def run():
    sys.stdout.write('\033[2J\033[1;1H')
    sys.stdout.flush()
    os.system('./build/src/client/client 127.0.0.1')

for i in range(2):
    threading.Thread(target=run).start()
