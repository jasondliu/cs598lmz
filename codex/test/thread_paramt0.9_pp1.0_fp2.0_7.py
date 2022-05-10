import sys, threading
threading.Thread(target=lambda:sys.stdout.write('hi\n'), args=()).start()
print('hello')
