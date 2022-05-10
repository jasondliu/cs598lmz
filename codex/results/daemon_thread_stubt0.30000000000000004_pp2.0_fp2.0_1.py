import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    print('Hello')
    thread.join()

if __name__ == '__main__':
    main()
