import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input().swapcase() + ' '),daemon=True).start()
'''

"""48
import threading
threading.Thread(target=lambda:print(*[input().swapcase() for _ in range(2)],sep=' ',end='')).start()
"""

"""49
import threading
t=threading.Thread(lambda:print(''.join(reversed(list(input())))))
t.start()
t.join()
"""

"""50
import threading
def reverse(s):
    return s[::-1]
t=threading.Thread(target=reverse,args=(input(),))
t.start()
t.join()
print(*t)
"""
