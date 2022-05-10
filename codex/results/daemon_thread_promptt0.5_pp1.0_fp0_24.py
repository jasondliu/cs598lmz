import threading
# Test threading daemon mode
#
# @author yingzhuo.chen
# @date 2016-08-07

def do_something(s):
    print(s)

def main():
    t = threading.Thread(target=do_something, args=('hello',))
    t.setDaemon(True)
    t.start()

    print('main thread')

if __name__ == '__main__':
    main()
