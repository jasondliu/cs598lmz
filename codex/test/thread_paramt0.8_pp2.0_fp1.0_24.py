import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()
'''

'''
import sys, threading
threading.Thread(target=lambda: sys.stdin.read(), args=(), kwargs={}).start()
'''

'''
import sys, threading
threading.Thread(target=sys.stdin.read, args=(), kwargs={}).start()
'''

'''
import sys, threading
if __name__ == '__main__':
    threading.Thread(target=lambda: sys.stdin.read()).start()
'''

'''
import sys, threading
if __name__ == '__main__':
    threading.Thread(target=lambda: sys.stdin.read(), args=(), kwargs={}).start()
'''

'''
import sys, threading
if __name__ == '__main__':
    threading.Thread(target=sys.stdin.read, args=(), kwargs={}).start()
'''

'''
import sys, threading
