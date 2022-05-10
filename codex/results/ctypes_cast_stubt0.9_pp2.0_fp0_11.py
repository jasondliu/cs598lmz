import ctypes
ctypes.cast(mem, ctypes.py_object).value = (1,2,3,4,5)


q=mpi.world.request()
q.Isend([0,1,2], dest=1, tag=77)
q.Isend([3,4], dest=1, tag=88)
q.Wait()
</code>
Note, with MPICH, you cannot have <code>Intercomm_merge</code> after a <code>Intercomm_create</code>.  With OpenMPI, it appears, you must have an <code>Intercomm_merge</code>.

