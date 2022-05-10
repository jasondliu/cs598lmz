import threading
# Test threading daemon


class MyThread(threading.Thread):
    def __init__(self, name, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.name = name

    def run(self):
        print('{} starting'.format(self.name))
        time.sleep(2)
        print('{} ending'.format(self.name))


def main():
    for i in range(3):
        t = MyThread(name='thread_{}'.format(i))
        t.setDaemon(True)
        t.start()

    print('main ending')


if __name__ == '__main__':
    main()
