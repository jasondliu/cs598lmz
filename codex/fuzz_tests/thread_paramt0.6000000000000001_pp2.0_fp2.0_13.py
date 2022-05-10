import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

print('Hello from main thread')

#-----------------------------------------------------------------------------------------------------------------------

#print('Hello from main thread')
#
#import sys, threading
#
#def do_something(data):
#    print(data)
#
#threading.Thread(target=do_something, args=('Hello from thread 1',)).start()
#threading.Thread(target=do_something, args=('Hello from thread 2',)).start()
#
#print('Hello from main thread')

#-----------------------------------------------------------------------------------------------------------------------

#print('Hello from main thread')
#
#import sys, threading
#
#class MyThread(threading.Thread):
#    def run(self):
#        print('Hello from thread')
#
#threading.Thread(target=MyThread()).start()
#
#print('Hello from main thread')

#-----------------------------------------------------------------------------------------------------------------------

#print('Hello
