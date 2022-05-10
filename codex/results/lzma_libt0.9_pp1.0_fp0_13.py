import lzma
lzma_opener = functools.partial(lzma.open, mode='rt')
 
# Pickle:
with opener('f.pkl', 'wb') as f:  # Use `opener()` wherever you would have used `open()`
    pickle.dump(data,f)

# Gzip:
with opener('f.gzip', 'wt') as f:  
    f.write(data)

# BZ2:
with opener('f.bz2', 'wt') as f:
    f.write(data)

# LZMA:
with opener('f.xz', 'wt') as f:
    f.write(data)
</code>



