import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello ')).start()
threading.Thread(target=lambda: sys.stdout.write('world!')).start()
 
"""

"""
def hello():
	print('hello world')		

thread_name=threading.current_thread().getName()
print(thread_name)

threading.Thread(target=hello, name='mythread').start()

"""



"""
#threading.Thread(target=sys.stdout.write, args=('hello ',)).start()
#threading.Thread(target=sys.stdout.write, args=('world!',)).start()

"""


"""

def hello():
	print('hello')

threading.Thread(target=lambda: print('hello world')).start()

threading.Thread(target=lambda: sys.stdout.write('hello ')).start()
threading.Thread(target=lambda: sys.stdout.write('world! ')).start()

"""



"""
import sys, threading

def hello():
	print
