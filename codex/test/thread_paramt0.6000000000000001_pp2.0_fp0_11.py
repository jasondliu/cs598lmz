import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
# Hello
threading.Thread(target=lambda: sys.stdout.write('Python\n')).start()
# Python
threading.Thread(target=lambda: sys.stdout.write('World\n')).start()
# World
