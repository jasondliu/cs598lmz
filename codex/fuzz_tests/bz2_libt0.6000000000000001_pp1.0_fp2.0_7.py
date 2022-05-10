import bz2
bz2.decompress(data).decode()

# %%
import re
pattern = re.compile(r'(.)\1*')
pattern.findall(data)

# %%
pattern = re.compile(r'(.)\1+')
pattern.findall(data)

# %%
import datetime
datetime.datetime.strptime('2018-01-01', '%Y-%m-%d')

# %%
datetime.datetime.strptime('2018-01-01', '%Y-%m-%d').date()

# %%
datetime.datetime.strptime('2018-01-01', '%Y-%m-%d').time()

# %%
datetime.datetime.strptime('2018-01-01', '%Y-%m-%d').date()

# %%
import datetime
datetime.datetime.strftime('2018-01-01', '%Y-%m-%d')

# %%
import datetime
datetime.datetime.strftime('
