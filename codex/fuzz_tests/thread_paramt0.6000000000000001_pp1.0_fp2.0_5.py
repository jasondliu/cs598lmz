import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello\n")).start()

# Hello
# <Thread(Thread-1, started 140363830202368)>

threading.Thread(target=lambda:sys.stdout.write("Hello\n")).start().join()

# Hello
# <Thread(Thread-2, stopped 140363831845376)>

threading.Thread(target=lambda:sys.stdout.write("Hello\n")).start().join()

# Hello
# <Thread(Thread-3, stopped 140363830202368)>

threading.Thread(target=lambda:sys.stdout.write("Hello\n")).start().join()

# Hello
# <Thread(Thread-4, stopped 140363830202368)>

threading.Thread(target=lambda:sys.stdout.write("Hello\n")).start().join()

# Hello
# <Thread(Thread-5, stopped 140363830202368)>

threading.Thread(target=lambda:sys.stdout.write("Hello
