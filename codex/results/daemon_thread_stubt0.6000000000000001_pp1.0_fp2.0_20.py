import sys, threading

def run():
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

def main():
    threading.Thread(target=run).start()
    while True:
        print 'foo'
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>

