import bz2
bz2.BZ2File(path).readlines()

# In[ ]:


# pandas.read_csv()
import pandas as pd
df = pd.read_csv(path)
df.head()

# In[ ]:


# pandas.read_table()
import pandas as pd
df = pd.read_table(path, sep=',')
df.head()

# In[ ]:


# pandas.read_excel()
import pandas as pd
df = pd.read_excel(path, 'Sheet1')
df.head()

# In[ ]:


# pandas.read_hdf()
import pandas as pd
df = pd.read_hdf(path, 'df')
df.head()

# In[ ]:


# pandas.read_json()
import pandas as pd
df = pd.read_json(path, orient='columns')
df.head()

# In[ ]:


# pandas.read_msgpack()
