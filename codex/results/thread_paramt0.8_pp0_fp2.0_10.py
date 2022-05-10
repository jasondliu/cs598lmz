import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(map(str,
    filter(lambda n:sorted(str(n))==sorted(str(12*n)),
    range(10**4)
    ))))).start()
