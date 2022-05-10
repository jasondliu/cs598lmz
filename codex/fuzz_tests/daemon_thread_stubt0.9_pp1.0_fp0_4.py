import sys, threading

def run():
    while 1:
        print('working from thread %s' % threading.current_thread().name)
        sys.stdout.flush()
        time.sleep(0.5)
        print('work done from thread %s' % threading.current_thread().name)
        sys.stdout.flush()
        time.sleep(0.5)

def main():

    for i in range(5):
        t = threading.Thread(target=run, name="Thread-" + str(i))
        t.setDaemon(True)
        t.start()

main()
