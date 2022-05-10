import lzma
lzma.LZMACompressor()

# Install mpi4py
# Note: because the default mpi4py installation uses pip, we specify
# mpi=mpich rather than mpi=openmpi.
# Also, openmpi must be built with --enable-mpi-cxx
