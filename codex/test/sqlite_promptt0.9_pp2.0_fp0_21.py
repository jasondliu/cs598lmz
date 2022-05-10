import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect_multithreaded()

class MyThread(threading.Thread):
    def run(self):
        print(self.getName(), ": Open database")
        con = sqlite3.connect(":memory:", check_same_thread=False)
        con.close()
        print(self.getName(), ": OK")


def main():
    # Create several threads and start them
    t1 = MyThread(name="T1")
    t2 = MyThread(name="T2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")

if __name__ == "__main__":
    main()
