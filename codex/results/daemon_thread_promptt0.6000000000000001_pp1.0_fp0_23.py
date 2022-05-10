import threading
# Test threading daemon
#

def test_daemon():
    t = threading.Thread(target=daemon_func, args=('daemon',))
    t.setDaemon(True)
    t.start()
    print('Main thread end')
    return


def daemon_func(name):
    for i in range(10):
        print('{} thread {}'.format(name, i))
        time.sleep(1)
    return


if __name__ == '__main__':
    test_daemon()
