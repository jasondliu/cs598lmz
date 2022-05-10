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
"""

# import threading
# def run():
#     for i in range(5):
#         print('thread')
# threading.Thread(target=run).start()
# threading.Thread(target=run).start()
# threading.Thread(target=run).start()

# import os, threading
# def open_file():
#     os.system('start notepad')
#
# threading.Thread(target=open_file).start()

# import time
# print('Start')
# time.sleep(5)
# print('end')

# for i in range(5):
#     time.sleep(1)
#     print('thread')
# print('main')

# import threading
# def run():
#     for i in range(5):
