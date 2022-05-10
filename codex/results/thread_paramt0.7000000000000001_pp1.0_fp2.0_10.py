import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a different thread!\n")).start()

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(5)
