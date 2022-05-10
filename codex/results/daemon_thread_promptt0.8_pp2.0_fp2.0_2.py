import threading
# Test threading daemon
def worker():
    print('worker')
    # time.sleep(1)
    print('worker done')

# t = threading.Thread(target=worker)
# t.start()

# t.join()
# print('main thread')

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def test():
    print('test')

def test2():
    print('test2')

def test3():
    print('test3')
    raise RuntimeError()

def test4():
    print('test4')


def test5():
    print('test5')
    return 1

def test6():
    print('test6')
    return 2

def test7():
    print('test7')
    return 3

def test8():
    print('test8')
    return 4

def main():

