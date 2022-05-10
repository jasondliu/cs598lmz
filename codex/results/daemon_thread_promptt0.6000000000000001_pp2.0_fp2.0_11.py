import threading
# Test threading daemon mode

def foo():
    print("foo")
    gevent.sleep(1)
    print("foo end")
    return 'foo'

def bar(arg):
    print("bar {}".format(arg))
    gevent.sleep(2)
    print("bar end")

def main():
    threading.Thread(target=bar, args=('test',)).start()
    print("main end")

if __name__ == '__main__':
    main()
