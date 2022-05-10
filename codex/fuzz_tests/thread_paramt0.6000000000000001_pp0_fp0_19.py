import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(input()[::-1] for _ in range(int(input()))))).start()

# from sys import stdin, stdout
# stdout.write('\n'.join(stdin.read()[::-1] for _ in range(int(input()))))

# from sys import stdin, stdout
# stdout.write('\n'.join(stdin.read()[::-1] for _ in range(int(input()))))

# from sys import stdin, stdout
# stdout.write('\n'.join(stdin.read()[::-1] for _ in range(int(input()))))
