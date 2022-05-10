from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# %%
from bz2 import BZ2File
with BZ2File('myfile.bz2', 'w') as f:
    f.write(data)
with BZ2File('myfile.bz2', 'r') as f:
    f.read()

# %%
import bz2
with open('file.bz2', 'rb') as f:
    # decompress as you go
    data = bz2.decompress(f.read())

# %%
from bz2 import BZ2File
from io import BytesIO
from tqdm import tqdm
with BZ2File('myfile.bz2', 'r') as f:
    for line in tqdm(f.readlines()):
        # Do something with line
        pass

# %%
from bz2 import BZ2File
from tqdm import tqdm
from functools import partial
with BZ2File('myfile.bz2', 'r') as f:
