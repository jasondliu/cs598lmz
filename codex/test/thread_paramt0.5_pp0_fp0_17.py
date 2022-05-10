import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()

# Q-70: What is the output of the following Python code?
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
# sys.stdout.write('World\n')

# Q-71: What is the output of the following Python code?
# import threading
# def hello():
#     print('Hello')
# t = threading.Thread(target=hello)
# t.start()
# print('World')

# Q-72: What is the output of the following Python code?
# import threading
# def hello():
#     print('Hello')
# t = threading.Thread(target=hello)
# t.start()
# t.join()
# print('World')

# Q-73: What is the output of the following Python code?
# import threading
# def hello():
#     print('Hello')
# t = threading.Thread(target=hello)
# t.start()
#
