import select
# Test select.select with a FIFO

msg = "x" * 1024

with tempfile.TemporaryDirectory() as tmpdir:
    fifoname = os.path.join(tmpdir, 'fifo')
    os.mkfifo(fifoname)
    f = open(fifoname, 'wb')
    pid = os.fork()
    if pid == 0:
        time.sleep(1)
        f2 = open(fifoname, 'rb')
        print('CHILD: opened for reading', fifoname)
        data = f2.read()
        print('CHILD: read', len(data), 'bytes')
        sys.stdout.flush()
        f2.close()
        os._exit(0)
    else:
        print('PARENT: opened for writing', fifoname)
        f.write(msg)
        print('PARENT: writing to pipe')
        f.close()
        print('PARENT: closed pipe')
        _, _, _ = os.waitpid(pid, 0)
        print('PARENT: exit')
