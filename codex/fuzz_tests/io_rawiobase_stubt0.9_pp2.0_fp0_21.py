import io
class File(io.RawIOBase):
    def __init__(self, path, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)

    def readline(self):
        return b'line'


def list_files(proc):
    files = []
    for fd in proc.fd_dir.fdList():
        procinfo = cmdline.ProcInfo(fds={fd: open(fd.path())})
        if procinfo.command == 'python':
            files.append(File(proc.fd_dir.fdPath(fd)))
    return files


with open('trace.log', 'w') as f:
    tracer = Trace(f, trace=0)
    tracer.runfunc(test, 5)

import threading
import multiprocessing

threads = [threading.Thread(target=test, args=(3,)) for _ in range(10)]
processes = [multiprocessing.Process(target=test, args=(3,)) for _ in range(10)]

for t in threads:
    t.
