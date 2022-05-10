import bz2
bz2.BZ2File('data/train.bz2', 'r')

with bz2.BZ2File('data/train.bz2', 'r') as f:
    for line in f:
        print(line)
        break

# %%
import pandas as pd

df = pd.read_csv('data/train.bz2', sep='\t')
df.head()

# %%
df = pd.read_csv('data/train.bz2', sep='\t', nrows=10)
df.head()

# %%
import bz2
import pandas as pd

with bz2.BZ2File('data/train.bz2') as f:
    for i in range(5):
        print(f.readline().decode('utf-8'))

# %%
import bz2
import pandas as pd

with bz2.BZ2File('data/train.bz2') as f:
    for df in pd.read_csv(f, sep
