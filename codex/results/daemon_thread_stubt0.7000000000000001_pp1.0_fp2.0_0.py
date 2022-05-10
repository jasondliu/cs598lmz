import sys, threading

def run():
    print('thread start')
    print(sys.getrefcount(2))
    sys.exit()
    print('thread end')

t = threading.Thread(target=run)
print(sys.getrefcount(2))
t.start()
t.join()
print(sys.getrefcount(2))
