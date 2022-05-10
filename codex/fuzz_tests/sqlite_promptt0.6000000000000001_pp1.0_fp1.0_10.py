import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class MyThread(threading.Thread):
    def __init__(self, db, mutex):
        threading.Thread.__init__(self)
        self.db = db
        self.mutex = mutex
        self.stopped = False

    def run(self):
        while not self.stopped:
            self.mutex.acquire()
            try:
                self.db.execute('select * from test')
            except Exception, e:
                print e
            self.mutex.release()

def main():
    db = sqlite3.connect(':memory:')
    db.execute('create table test (id integer)')
    db.commit()

    mutex = threading.Lock()
    for i in range(100):
        t = MyThread(db, mutex)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
