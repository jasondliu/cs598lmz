import sys, threading
threading.Thread(target=lambda:sys.stdout.write('hello\n'), daemon=True).start()
'''
while True:
    pass  # <2>
