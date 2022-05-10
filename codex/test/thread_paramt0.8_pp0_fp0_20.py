import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

sys.stdout.write('Hello world\n')
sys.stdout.flush()

# sys.stdout = open('1.txt', 'w')
# print('Hello world')

# def hello():
#     print('Hello world')
#
# sys.stdout = open('1.txt', 'w')
# hello()

# hello()
# new_stdout = sys.stdout
# new_stdout.write('hello world!\n')
# new_stdout.flush()
#
# f = open('1.txt', 'w')
# sys.stdout = f
# print('hello world')
