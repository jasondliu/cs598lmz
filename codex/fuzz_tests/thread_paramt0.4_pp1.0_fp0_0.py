import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# The output of this program will be:
# Hello from thread 1
# Hello from thread 2

# The output of this program will be:
# Hello from thread 2
# Hello from thread 1

# The output of this program will be:
# Hello from thread 1
# Hello from thread 1

# The output of this program will be:
# Hello from thread 2
# Hello from thread 2

# The output of this program will be:
# Hello from thread 1
# Hello from thread 2
# Hello from thread 1
# Hello from thread 2

# The output of this program will be:
# Hello from thread 1
# Hello from thread 2
# Hello from thread 2
# Hello from thread 1

# The output of this program will be:
# Hello from thread 1
# Hello from thread 1
# Hello from thread 2
# Hello from thread 2

# The output of this program will be:
# Hello
