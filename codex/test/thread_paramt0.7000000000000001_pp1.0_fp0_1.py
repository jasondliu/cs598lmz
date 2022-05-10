import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading!\n')).start()
print('Hello world!')
 
#threading.Thread(target=lambda: sys.stdout.write('Threading!\n')).start()
#print('Hello world!')

#Hello world!
#Threading!
