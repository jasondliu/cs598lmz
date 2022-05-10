import sys, threading

def run():
    try:
        while True:
            sys.stdout.write('1')
            sys.stdout.flush()
            time.sleep(0.5)
    except:
        pass

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        sys.stdout.write('2')
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
