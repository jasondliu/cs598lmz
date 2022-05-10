import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    t = threading.Thread(target = run)
    t.start()
    time.sleep(2)
    t.join()

if __name__ == '__main__':
    main()
