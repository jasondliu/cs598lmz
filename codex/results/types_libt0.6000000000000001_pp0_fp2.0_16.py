import types
types.SimpleNamespace()

# %%
import requests

res = requests.get('https://www.baidu.com')
res.status_code
res.text

# %%
import time
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# %%
import os
os.mkdir('/tmp/a/b/c')

# %%
import os
os.makedirs('/tmp/a/b/c')

# %%
import os
os.removedirs('/tmp/a/b/c')

# %%
import os
os.rmdir('/tmp/a/b/c')

# %%
import os
os.path.isdir('/tmp/a')

# %%
import os
os.path.isfile('/tmp/a')

# %%
import os
os.path.exists('/tmp/a')

# %%
import os
os.path.
