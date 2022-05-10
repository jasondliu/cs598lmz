import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
print('Hello from thread 2')

# The same in PyPy
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
print('Hello from thread 2')

# The same in Jython
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
print('Hello from thread 2')

# The same in IronPython
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
print('Hello from thread 2')

# The same in IronPython
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
print('Hello from thread 2')

# The same in Ruby
Thread.new { puts 'Hello from thread 1' }
puts 'Hello from thread 2'

# The same
