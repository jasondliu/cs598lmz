import sys, threading

def run():
    sys.stdout.write('_')
    sys.stdout.flush()
    time.sleep(1)

def main():
    while True:
        thread = threading.Thread(group=None, target=run)
        thread.start()
        thread.join()

if __name__ == '__main__':
    main()
