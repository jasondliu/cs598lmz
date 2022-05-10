import select
# Test select.select()
print('select.select:')
for i in range(m.get_cpu_count()):
    print('\tCPU{}: {}'.format(i, select.select([], [], [], 0)))

# Test multiprocessing.Queue
from multiprocessing import Queue as mQueue
print('multiprocessing.Queue:')
for i in range(m.get_cpu_count()):
    print('\tCPU{}: {}'.format(i, mQueue().empty()))

# Test multiprocessing.Pipe
from multiprocessing import Pipe as mPipe
print('multiprocessing.Pipe:')
for i in range(m.get_cpu_count()):
    r, w
