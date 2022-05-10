import lzma
lzma.decompress(data)

# In[ ]:


import gzip
import io
s = io.BytesIO(data)
with gzip.GzipFile(fileobj=s) as f:
    text = f.read()


# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
from scipy.cluster.hierarchy import ward, dendrogram


# In[ ]:


from scipy.cluster import hierarchy
distance = 1 - cosine_similarity(tfidf_matrix)


# In[ ]:


Z = hierarchy.linkage(distance, 'ward')


# In[ ]:


import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster

# k = 5
clusters = fcluster(Z, 5
