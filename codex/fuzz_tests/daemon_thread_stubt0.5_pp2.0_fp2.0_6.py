import sys, threading

def run():
    while True:
        sys.stdout.write('hello\n')
        sys.stdout.flush()
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        sys.stdout.write('world\n')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>

