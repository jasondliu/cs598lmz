import sys, threading

def run():
    ret = 'Hello'

    return ret

class MyThread(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.setDaemon(True)

    def run(self):
        ret = run()
        print(ret)

if __name__ == '__main__':
    MyThread().start()
    time.sleep(1)
    print('Good bye')
</code>

