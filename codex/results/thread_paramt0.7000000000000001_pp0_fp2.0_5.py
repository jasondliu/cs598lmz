import sys, threading
threading.Thread(target=lambda:sys.stdout.write(input())).start()

# from time import sleep, time
# from sys import stdin
# start = time()
# sleep(2)
# sys.stdout.write(stdin.read())
# print 'Elapsed:', time() - start
