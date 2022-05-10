import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

print('main')

import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')


print('#'*52 + '  #')
print('#'*52 + '  #')
print('#'*52 + '  #')
print('#'*52 + '  #')
print('#'*52 + '  #')
print('#'*52 + '  #')
print('#'*52 + '  #')

import sys, threading
sys.stdout.write('thread')
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

print('main')

import sys, threading
sys.stdout.write('thread')
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')

# # Output
# main
# thread


# # Output
# thread
#
