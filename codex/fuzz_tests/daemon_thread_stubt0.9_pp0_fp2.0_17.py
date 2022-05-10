import sys, threading

def run():
    while True:
        if sys.stdin.read(1) != '\n':
            gdb.execute('quit')
            print('\n--- Stopped (remote control) ---\n')

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()
gdb.execute('set height 0')
