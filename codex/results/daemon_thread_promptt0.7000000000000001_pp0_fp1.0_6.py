import threading
# Test threading daemon mode
threadLocal = threading.local()

def get_current_user():
    return getattr(threadLocal, 'user', None)

class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

def test(id, name):
    user = User(id, name)
    threadLocal.user = user
    get_current_user()
    print(threading.current_thread().getName())

for i in range(5):
    t = threading.Thread(target=test, args=(i, 'test' + str(i)))
    t.setDaemon(True)
    t.start()

t.join()
print('main thread stop')
