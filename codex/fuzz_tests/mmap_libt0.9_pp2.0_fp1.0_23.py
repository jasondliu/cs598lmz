import mmap
import posix_ipc
import shm_wrapper
from shm_wrapper import *

this_addr = './test.data1'
peer_addrs = ['./test.data2']

# Initialize shared memory, parameter: <total shared memory, read-only shared memory, write-only shared memory>
# Be aware that variable this_addr must be string type, or it will cause error
shm = shm_wrapper(this_addr, peer_addrs)

SHM_SIZE = SHM_MAX_SIZE

# Now we get the shared memory
global_shm = shm.global_shm

# example shared memory
q1 = mmap.mmap(global_shm, SHM_SIZE, mmap.ACCESS_WRITE)  # map mmap_id
q2 = mmap.mmap(global_shm, SHM_SIZE, mmap.ACCESS_READ)  # map mmap_id

time.sleep(1)

while True:
    string = q2.read(SHM_SIZE)
    print("
