import lzma
lzma.LZMACompressor()

# Install mpi4py
# Note: because the default mpi4py installation uses pip, we specify
# mpi=mpich rather than mpi=openmpi.
# Also, openmpi must be built with --enable-mpi-cxx
module load openmpi/2.0.1
module load python/2.7.9
cd ../python
CC=mpicc CXX=mpicxx pip install -r requirements.txt
pip install -r requirements.txt
python setup.py install

# Install image-analysis-tools
cd ../image-analysis-tools
CC=mpicc CXX=mpicxx pip install -r requirements.txt
pip install -r requirements.txt
python setup.py install

# Install htmap
cd ../htmap
pip install -r requirements.txt
python setup.py install

# Install dask
cd ../dask
pip install .

# Install matplotlib
cd ../matplotlib
pip install .

# Install zarr
cd ../zarr
