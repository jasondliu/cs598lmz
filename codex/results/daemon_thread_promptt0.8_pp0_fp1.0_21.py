import threading
# Test threading daemon mode
class do_sleep(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        print(self.getName(), 'start')
        time.sleep(2)
        print(self.getName(), 'stop')

thread = do_sleep()
thread.start()

print('Waiting...')
thread.join()
print('End')

class add_num(threading.Thread):

    def __init__(self, a, b, callback):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.callback = callback

    def run(self):
        print(self.getName(), 'start')
        self.callback(self.a + self.b)
        print(self.getName(), 'stop')

def fn_callback(result):
    print('The result is:', result)

thread = add_num(1, 2, fn_callback)
thread
