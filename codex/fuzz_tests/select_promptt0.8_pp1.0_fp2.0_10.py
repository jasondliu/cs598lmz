import select
# Test select.select()
print('Starting')
import sys, time
time.sleep(0.25)
print('Loop starting')
sys.stdout.flush()
start = time.time()
for i in range(5):
    print('Blocking %s' % i)
    sys.stdout.flush()
    # select.select([sys.stdin], [], [], 0.0001)
    time.sleep(0.25)
print('Loop ended in %.02f seconds' % (time.time() - start))
