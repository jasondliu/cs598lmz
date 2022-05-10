import bz2
bz2.decompress(file_content)

# In[ ]:

#To simplify the process, we can use the io package and wrap the file in a io.BytesIO stream

import io
import bz2

with open('data/file.bz2', 'rb') as f:
    file_content = f.read()
    uncompressed_data = bz2.decompress(file_content)
    print(uncompressed_data)

# In[ ]:

# compress data
data = b'This is the data to compress'
compressed = bz2.compress(data)
print(compressed)

# In[ ]:

#decompress data
import bz2
uncompressed = bz2.decompress(compressed)
print(uncompressed)

# In[ ]:

# Compress a file
import bz2
with open('data/file.txt', 'rb') as input:
    print('input has {0} bytes'.format(len(input.read())))
    with bz2.
