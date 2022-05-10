import bz2
bz2.BZ2File(file_path)

# %%
import os
os.path.getsize(file_path)

# %%
file_bz2 = bz2.BZ2File(file_path)
data = file_bz2.read()

# %%
type(data)

# %%
len(data)

# %%
file_bz2 = bz2.BZ2File(file_path)
for line in file_bz2:
    print(line)

# %%
import json
records = [json.loads(line) for line in file_bz2]

# %%
len(records)

# %%
records[0]

# %%
records[0]['tz']

# %%
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

# %%
time_zones[:10]

# %%
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
           
