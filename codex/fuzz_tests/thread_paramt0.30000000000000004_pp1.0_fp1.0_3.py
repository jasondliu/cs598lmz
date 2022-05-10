import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# 3.2
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# sys.stdout.write("world\n")

# 3.3
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# sys.stdout.write("world\n")
# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# 3.4
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# sys.stdout.write("world\n")
# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# sys.stdout.write("world\n")

# 3.5
# import sys, threading
# threading.Thread(target=lambda: sys
