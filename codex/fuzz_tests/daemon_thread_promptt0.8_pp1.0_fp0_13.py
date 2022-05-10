import threading
# Test threading daemon
def func():
    while True:
        print('nein')
        time.sleep( 1 )
t1 = threading.Thread( target=func )
t1.daemon = True
t1.start()
# Comment to continue testing
sys.exit( 0 )
# Does not work:
def func():
    for i in range( 10 ):
        print( 'nein' )
        time.sleep( 1 )
t1 = threading.Thread( target=func )
t1.daemon = True
t1.start()
t1.join()
# Does not work:
t1 = threading.Thread( target=func )
t1.daemon = True
t1.join()
t1.start()
# Works:
t1 = threading.Thread( target=func )
t1.daemon = True
t1.start()
t1.join()
# Works:
t1 = threading.Thread( target=func )
t1.join()
t1.daemon = True
t1.start()
