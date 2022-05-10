import threading
# Test threading daemon usage:
#
#import gevent
#
#EVENT = threading.Event()
#
## this function needs to run in a thread
#def async_function(name):
#    print '%s is waiting...' % name
#    EVENT.wait()
#    print '%s resumed' % name
#
## this function needs to run in a separate greenlet
#def controlling_function(async_function, *args):
#    gevent.sleep(0.1)
#    print 'Notifying...'
#    EVENT.set()
#    async_function(*args)
#
#def main():
#    print 'main started'
#    t = threading.Thread(target=async_function, args=('async_function',))
#    d = gevent.spawn(controlling_function, async_function, 'async_function')
#    t.start()
#    d.join()
#    print 'main done'
#
#if __name__ == '__main__':
#    main()

class DataDealThread(threading.
