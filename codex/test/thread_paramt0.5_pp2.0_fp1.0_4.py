import sys, threading
threading.Thread(target=lambda: sys.stdout.write("a")).start()
threading.Thread(target=lambda: sys.stdout.write("b")).start()

# a
# b

# threading.Thread(target=lambda: sys.stdout.write("a")).start()
# threading.Thread(target=lambda: sys.stdout.write("b")).start()
# threading.Thread(target=lambda: sys.stdout.write("c")).start()

# a
# b
# c

# threading.Thread(target=lambda: sys.stdout.write("a")).start()
# threading.Thread(target=lambda: sys.stdout.write("b")).start()
# threading.Thread(target=lambda: sys.stdout.write("c")).start()
# threading.Thread(target=lambda: sys.stdout.write("d")).start()

# a
# b
# c
# d

# threading.Thread(target=lambda: sys.stdout.write("a")).start()
# threading
