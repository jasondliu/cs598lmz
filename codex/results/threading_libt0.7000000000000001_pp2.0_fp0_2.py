import threading
threading.stack_size(1024*1024*8)
import time

def td():
    now=datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    time.sleep(1)
    print("threading ")

my_thread = threading.Thread(target=td)
my_thread.start()

# 如果不加这句，main thread会退出，从而导致程序退出
my_thread.join()
