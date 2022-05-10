import sys, threading
threading.Thread(target=lambda: sys.stdout.write("This is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("right before\n")).start()
threading.Thread(target=lambda: sys.stdout.write("This is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("this is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("right after\n")).start()

# This is printed
# right before
# this is printed
# This is printed
# right after
