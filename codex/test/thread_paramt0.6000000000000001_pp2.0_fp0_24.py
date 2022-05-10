import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('thread2\n')).start()
print('main')

# main
# thread2
# thread1

# thread1
# main
# thread2

# thread2
# main
# thread1

# main
# thread1
# thread2

