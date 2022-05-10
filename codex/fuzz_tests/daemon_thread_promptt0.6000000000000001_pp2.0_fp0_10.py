import threading
# Test threading daemon

def main():
    p = Process(target=hello)
    p.daemon = True
    p.start()
    while True:
        time.sleep(0.1)

def hello():
    while True:
        print 'hello'
        time.sleep(1)

if __name__ == '__main__':
    main()
