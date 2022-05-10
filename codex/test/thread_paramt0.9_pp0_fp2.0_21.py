import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

print('foo')

# Output:
# .foo
