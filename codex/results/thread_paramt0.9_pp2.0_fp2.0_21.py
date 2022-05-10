import sys, threading
threading.Thread(target=lambda: sys.stdout.write(
                 'threadY\n')).start()
print('foo') #prints after 'threadY', unless priority set
