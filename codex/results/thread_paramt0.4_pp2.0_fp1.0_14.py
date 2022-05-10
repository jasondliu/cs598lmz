import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# This is a thread that will be started and will run in the background.
# It will print a newline every second.

# You can run the following code to see the output of this program:
# python3 -m doctest -v solution.py
# after
# python3 solution.py
