import threading
threading.Thread(target=hello,args=(1,2,3)).start()
import time
# def timer(n):
#     while True:
#         print(n)
#         time.sleep(1)
# t=threading.Thread(target=timer,args=(1,))
# t.daemon=True
# t.start()
import time
def iodemo():
    print('start demo')
    time.sleep(4)
    print('end demo')
# t=threading.Thread(target=iodemo)
# t.start()
# t.join()
import gevent
def foo():
    print('running in foo')
    gevent.sleep(3)
    print('switch to foo again')
def bar():
    print('switch to bar')
    gevent.sleep(3)
    print('switch to bar again')
# gevent.joinall([gevent.spawn(foo),gevent.spawn(bar)])#协程
# gevent.joinall([gevent.spawn(foo),gevent.spawn(foo)])
#
