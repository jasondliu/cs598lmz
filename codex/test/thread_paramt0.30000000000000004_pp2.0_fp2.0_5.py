import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()

# Python 3.8
# import sys, threading
# threading.Thread(target=sys.stdout.write, args=("Hello World\n",)).start()

# Python 3.8
# import sys, threading
# threading.Thread(target=sys.stdout.write, args=("Hello World\n",), daemon=True).start()

# Python 3.8
# import sys, threading
# threading.Thread(target=sys.stdout.write, args=("Hello World\n",), daemon=True, name="Hello").start()

# Python 3.8
# import sys, threading
# threading.Thread(target=sys.stdout.write, args=("Hello World\n",), daemon=True, name="Hello").start()
# print("Hello" in threading.enumerate())

# Python 3.8
# import sys, threading
# threading.Thread(target=sys.stdout.write, args=("Hello World\n",), daemon=True
