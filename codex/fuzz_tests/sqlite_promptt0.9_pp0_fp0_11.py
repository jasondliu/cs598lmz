import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
def test():
    retries = 10
    curdir = os.getcwd()
    print(curdir)
    while retries > 0:
        try:
            conn = sqlite3.connect(os.path.join(os.getcwd(), 'test.db'))
            cur = conn.cursor()
            cur.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL,
                ADDRESS        CHAR(50),
                SALARY         REAL);''')
            conn.commit()
            break
        except:
            retries -= 1
            print('Locked. Retry ' + str(retries - 1))
            sleep(0.1)
    conn.close()
# Create a thread to open the database file
t = threading.Thread(target=test)
t.start()
# Print the current directory
print(ctypes.util.find_library('c'))
# Print the current directory and the path to libc.
