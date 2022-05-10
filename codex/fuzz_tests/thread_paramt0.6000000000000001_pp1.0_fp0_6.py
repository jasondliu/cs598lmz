import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
threading.Thread(target=lambda: sys.stdout.write("world\n")).start()

# $ python
# >>> import sys, threading
# >>> threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# >>> threading.Thread(target=lambda: sys.stdout.write("world\n")).start()
# hello
# world

# threading.Thread(target=lambda: sys.stdout.write("hello\n")).run()
# threading.Thread(target=lambda: sys.stdout.write("world\n")).run()
# hello
# world

# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# threading.Thread(target=lambda: sys.stdout.write("world\n")).start()
# hello
# world

# threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
# threading.Thread
