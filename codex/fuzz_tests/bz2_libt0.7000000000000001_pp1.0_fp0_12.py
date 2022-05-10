import bz2
bz2.BZ2File(pagina)

# In[5]:


#especificando o tipo de arquivo
import bz2
with bz2.BZ2File('pagina.html.bz2') as pagina:
    conteudo = pagina.read()


# In[6]:


#usando o context manager
import bz2
with bz2.BZ2File('pagina.html.bz2') as pagina:
    for linha in pagina:
        print(linha)


# In[7]:


#usando api do gzip
import gzip
with gzip.open('pagina.html.gz') as pagina:
    conteudo = pagina.read()


# In[8]:


#usando o context manager
import gzip
with gzip.open('pagina.html.gz') as pagina:
    for linha in pagina:
        print(linha)


# In[9]:


#usando zipfile.ZipFile

