import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# from sys import stdin, stdout
# threading.Thread(target=lambda: stdout.write(stdin.read())).start()

# from sys import stdin, stdout
# t = threading.Thread(target=lambda: stdout.write(stdin.read()))
# t.start()
# t.join()

# from sys import stdin, stdout
# stdout.write(stdin.read())

# from sys import stdin, stdout
# [stdout.write, stdin.read]()

# from sys import stdin, stdout
# stdout.write(stdin.read())

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# import sys
# sys.stdout.write(sys.stdin.read())

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())
