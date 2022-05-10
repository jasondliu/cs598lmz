import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

# 6.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\a')).start()
# print('\a')

# 7.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\a')).start()
# print('\a', end='')

# 8.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\a')).start()
# print('\a', end='', flush=True)

# 9.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\a')).start()
# print('\a', end='', flush=False)

# 10.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\a')).start()
# print('\a', end='', flush=True)
#
