import threading
# Test threading daemon for disk IO

#log_dir = '/Users/saya/Downloads/10.186.73.35-logs/'
from retrying import retry

from distalgo.runtime.udp import UdpRuntime
r = UdpRuntime()
r.start()

def getFileName(index, no_tasks, files):
    f_idx = index % 12
    if f_idx < 4:
        return files[f_idx]
    elif f_idx < 8:
        taskid = (index / 4) % no_tasks
        return '{0}/worker-{1}-1.txt'.format(log_dir, taskid)
    else:
        taskid = (index / 4) % no_tasks
        return '{0}/worker-{1}-2.txt'.format(log_dir, taskid)

@retry(wait_fixed=10)
def getIoLoad(files, no_tasks):
    #files = ['pio-test0.txt',
    #         'p
