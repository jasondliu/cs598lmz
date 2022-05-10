import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

# from multiprocessing import Process, Lock
# from ctypes import c_char_p
# from time import sleep

# def f(lock, message):
#     lock.acquire()
#     print(message)
#     lock.release()

# if __name__ == '__main__':
#     lock = Lock()
#     message = c_char_p("Hello, World!".encode("utf-8"))

#     p = Process(target=f, args=(lock, message))
#     p.start()
#     p.join()

# import multiprocessing as mp
# import time

# def washer(dishes, output):
#     for dish in dishes:
#         print('Washing', dish, 'dish')
#         output.put(dish)

# def dryer(input):
#     while True:
#         dish = input.get()
#         print('Drying', dish, 'dish')
#         input.task_
