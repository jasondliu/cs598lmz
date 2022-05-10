import lzma
lzma.decompress(open("./2.lzma", "rb").read())


# In[ ]:


#解压缩rar
import rarfile
rarfile.RarFile("./3.rar")


# In[ ]:


#解压缩zip
import zipfile
zipfile.ZipFile("./4.zip")


# In[ ]:


#解压缩tar
import tarfile
tarfile.TarFile("./5.tar")


# In[ ]:


#解压缩bz2
import bz2
bz2.decompress(open("./6.bz2", "rb").read())


# In[ ]:


#解压缩tar.gz
import tarfile
tarfile.TarFile("./7.tar.gz")


# In[ ]:


#解压缩tar.bz2
import tarfile
tarfile.TarFile(
