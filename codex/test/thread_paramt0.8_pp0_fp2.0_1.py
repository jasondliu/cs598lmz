import sys, threading
threading.Thread(target=lambda: sys.stdout.write('in thread\n')).start()
print('after thread')
# time.sleep(0.1)
# print('before thread')
# threading.Thread(target=lambda: sys.stderr.write('in thread\n')).start()
# print('after thread')

'''
缺点：会阻塞主线程，直到子线程完成
'''

# with open('delete.txt','w') as f:
#     f.write('abc')
#
# print(os.listdir('.'))
#
# import pickle
#
# with open('delete.txt','rb') as f:
#     data = pickle.load(f)
#     print(data)
#
# print(os.listdir('.'))
# os.remove('delete.txt')
# print(os.listdir('.'))

# from tkinter import *
#
# Lab = Label
#
#
