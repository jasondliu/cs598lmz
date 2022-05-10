import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread-1')).start()
time.sleep(1)
threading.Thread(target=lambda: sys.stdout.write('Thread-2')).start()
time.sleep(1)
threading.Thread(target=lambda: sys.stdout.write('Thread-3')).start()
time.sleep(1)
threading.Thread(target=lambda: sys.stdout.write('Thread-4')).start()
time.sleep(1)
threading.Thread(target=lambda: sys.stdout.write('Thread-5')).start()
time.sleep(1)
Thread-15Thread-2Thread-3Thread-4
'''

# solution 2, use join() and lock



''' Q.6
Write a function filter_long_words() that takes a list of words and an integer n and returns a list of the words that are longer than n.
def filter_long_words(n):
    list_of_words = []
    count = 0
    for i in range(10):
        word = input('enter word:
