import sys, threading

def run():
    while True:
        print "hello"
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>

