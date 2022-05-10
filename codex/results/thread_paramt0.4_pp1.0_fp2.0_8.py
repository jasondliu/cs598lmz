import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# print('Hello World!')
# sys.stdout.flush()

# def read_input():
#     while True:
#         print(input())

# threading.Thread(target=read_input).start()

# print('Hello World!')
# sys.stdout.flush()
