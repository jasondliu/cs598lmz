import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.2)

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    while True:
        try:
            sys.stdout.write('\n')
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            print('\nBye')
            break

if __name__ == '__main__':
    main()
