import threading
# Test threading daemonic
def test_thread ():
    def f(i):
        while True:
            print(i)
            time.sleep(1)
    t = threading.Thread(target=f, args=[1])
    t.daemon = True
    t.start()
    print('end')
    time.sleep(1)

def read_db(dbname):
    def f():
        c = conn.cursor()
        c.execute('SELECT * FROM test')
        for row in c:
            print(row)
        c.close()
    conn = sqlite3.connect(dbname)
    t = threading.Thread(target=f)
    t.start()
    time.sleep(1)
    conn.close()

# Test threading with argument
def test_threading_with_argument ():
    def f(num):
        print(num)
        time.sleep(1)
    t = threading.Thread(target=f, args=[1])
    t.start()

if __name__ == '__main__':

