import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread started\n')).start()

if __name__ == '__main__':
    print('Main thread exiting')

# $ python3 threading_daemon.py
# Main thread exiting
# Thread started
