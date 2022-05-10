import ctypes
ctypes.cast(cl_program, ctypes.c_void_p).value

Memory = mcl.data.Memory
CL_MEM_READ_WRITE_COPY = Memory.CL_MEM_READ_WRITE_COPY
CL_MEM_WRITE_ONLY = Memory.CL_MEM_WRITE_ONLY
CL_MEM_READ_ONLY = Memory.CL_MEM_READ_ONLY
cl_koko_float1_2 = Memory.create_buffer(mcl.mem_flags.CL_MEM_READ_WRITE_COPY, size=(24,))
cl_koko_float1_1 = Memory.create_buffer(mcl.mem_flags.CL_MEM_READ_WRITE_COPY, size=(24,))
cl_koko_float2_2 = Memory.create_buffer(mcl.mem_flags.CL_MEM_READ_WRITE_COPY, size=(24,))
cl_koko_float2_1 = Memory.create_buffer(mcl.mem_flags.CL_
