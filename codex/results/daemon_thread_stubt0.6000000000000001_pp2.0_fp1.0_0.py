import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    raw_input()
    print 'Input received'
</code>

