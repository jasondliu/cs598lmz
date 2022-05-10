import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print('Tick')

def rank_process(v):
    rank = process_rank()
    if rank is None:
        print('Batch task commencing')
    else:
        print('Rank {} commencing'.format(rank))

    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    signal.signal(signal.SIGALRM, handler)

def batch_task(v, queue):
    for i in range(10):
        print('Batch task working')
        time.sleep(0.2)
    queue.put('Done')

if __name__ == '__main__':
    with start_cluster() as cluster:

        Q = cluster.queue(allocator='local_processes',
                          nprocessor=4,
                          nthread=4,
                          nbatch=2,
                          nbatch_process=2)

        batcher = Q.from_task(rank_process, batch_task, nbatch=10,
                              batch_arguments={'queue': Queue()
