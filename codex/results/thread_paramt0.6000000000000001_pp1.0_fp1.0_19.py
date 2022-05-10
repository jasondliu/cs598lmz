import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Beautiful\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Parallel\n')).start()
threading.Thread(target=lambda: sys.stdout.write('World\n')).start()
threading.Thread(target=lambda: sys.stdout.write('!\n')).start()

# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))
