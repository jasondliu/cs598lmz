import lzma
lzma.open(filename)

#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000

#%%

import bz2
bz2.open(filename)

#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000

#%%

import gzip
gzip.open(filename)

#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000

#%%

import zstandard as zstd
zstd.open(filename)

#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000
#%timeit -n 1000

#%%
