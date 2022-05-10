import mmap
import sys

mm = mmap.mmap(0, 1024*64, mmap.MAP_ANONYMOUS | mmap.MAP_SHARED, 
               prot=mmap.PROT_READ | mmap.PROT_WRITE, 
               flags = mmap.MAP_ANONYMOUS | mmap.MAP_SHARED)

pid = os.fork()
if pid == 0:
    for i in range(10):
        print("Read: %s" % mm.readline())
        sys.stdout.flush()
        time.sleep(2)
else:
    pid2 = os.fork()
    if pid2 == 0:
        for i in range(5):
            print("Write: %s" % i, file=mm)
            sys.stdout.flush()
            time.sleep(5)
    else:
        os.waitpid(pid, 0)
        os.waitpid(pid2, 0)

 

# %%
