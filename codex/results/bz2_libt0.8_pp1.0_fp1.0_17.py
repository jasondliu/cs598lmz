import bz2
bz2.decompress(bz2.compress(bytes(str(range(10)), "utf-8")))

# %%
import zlib
zlib.decompress(zlib.compress(bytes(str(range(10)), "utf-8")))

# %%
#3.3.3
import timeit
timeit.timeit(stmt="sys.getsizeof(100**100)", setup="import sys", number=100000)

# %%
timeit.timeit(stmt="100**100", setup="", number=100000)

# %%
#3.3.4
import pickle
data = pickle.dumps([1, 2, 3, "a", "b", "c"])
data

# %%
pickle.loads(data)

# %%
import json
json.dumps([1, 2, 3, "a", "b", "c"])

# %%
json.dump([1, 2, 3, "a", "b", "c"], open("json.txt", "w"))

# %%
json
