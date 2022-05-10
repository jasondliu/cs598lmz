import bz2
bz2.BZ2File("test.json.bz2").read()

import json
json.loads(bz2.BZ2File("test.json.bz2").read())

#%%
import json
import bz2
json.loads(bz2.BZ2File("test.json.bz2").read())

#%%
import json
import bz2
import pandas as pd
df = pd.DataFrame(json.loads(bz2.BZ2File("test.json.bz2").read()))

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df.head()

#%%
df
