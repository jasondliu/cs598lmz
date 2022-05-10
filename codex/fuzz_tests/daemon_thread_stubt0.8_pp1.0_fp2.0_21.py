import sys, threading

def run():
    sys.stdout.write('hello world\n')

t = threading.Thread(target=run)
t.start()
t.join()

# output
'''
hello world
'''
