import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
"""

"""
def run():
    for i in range(5):
        print('thread')

threading.Thread(target=run).start()
for i in range(5):
    print('main')
