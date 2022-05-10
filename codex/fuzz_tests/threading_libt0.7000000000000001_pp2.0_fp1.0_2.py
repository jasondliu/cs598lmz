import threading
threading.current_thread()

#%%
class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('thread {} is running...'.format(self.name))
        time.sleep(1)
        print('thread {} ended.'.format(self.name))

if __name__ == "__main__":
    print('thread {} is running...'.format(threading.current_thread().name))
    t = MyThread('my_thread')
    t.start()
    t.join()
    print('thread {} ended.'.format(threading.current_thread().name))
