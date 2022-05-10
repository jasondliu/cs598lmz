import sys, threading

def run():
    sys.stdin = open('/dev/tty')
    sys.stdout = open('/dev/tty', 'w')
    sys.stderr = open('/dev/tty', 'w')
    os.execlp('python', 'python', *sys.argv)

threading.Thread(target=run).start()
