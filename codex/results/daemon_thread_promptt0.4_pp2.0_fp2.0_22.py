import threading
# Test threading daemon
#
#
#
#

def test_daemon(name):
    print('[%s] start' % name)
    time.sleep(3)
    print('[%s] end' % name)

def main():
    t = threading.Thread(target=test_daemon, args=('test',))
    t.setDaemon(True)
    t.start()
    print('main thread end')

if __name__ == '__main__':
    main()
