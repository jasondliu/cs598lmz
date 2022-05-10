from lzma import LZMADecompressor
LZMADecompressor().decompress(x)

# %%
import tarfile
import io
import lzma
import bz2

with tarfile.open('/data/src/github.com/pandas-dev/pandas/pandas/tests/data/legacy_pickle/series.pickle.xz') as f:
    member = f.getmembers()[0]
    with f.extractfile(member) as g:
        with io.BytesIO(g.read()) as h:
            with lzma.open(h) as i:
                with bz2.open(i) as j:
                    print(j.read())

# %%
import pickle
pickle.loads(j.read())

# %%
import pickle
import lzma
import bz2

with open('/data/src/github.com/pandas-dev/pandas/pandas/tests/data/legacy_pickle/series.pickle.xz', 'rb') as f:
    with lzma.open(f)
