import ctypes
ctypes.cdll.LoadLibrary('libgomp.so')
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    A = np.arange(4)
    print(A)
    comm.Send(A, dest=1)
else:
    A = np.empty(5, dtype=int)
    comm.Recv(A, source=0)
    print(A)

A.ctypes.data

# send and recv will block until buffer is available
A = np.arange(4)
comm.Send(A, dest=1)
comm.Recv(A, source=1)
print(A)
