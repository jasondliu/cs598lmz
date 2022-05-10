import sys, threading

def run():
    print 'hello'

def main(threads):
    for i in range(threads):
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main(int(sys.argv[1]))
</code>

