import sys, threading
threading.Thread(target=lambda: sys.stdout.write("me\n")).start()
threading.Thread(target=lambda: sys.stdout.write("myself\n")).start()
threading.Thread(target=lambda: sys.stdout.write("I\n")).start()
