from lzma import LZMADecompressor
LZMADecompressor()
# if LZMADecompressor() throws an exception, then you need to install pyliblzma.
# see note above.

import numpy
numpy.__version__
# try again if you get "TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''"


import tensorflow
tensorflow.__version__
# on google compute engine and google colab, month_year is auto-installed. no-op here.




# In[ ]:


# PART 0 - download the data (for everyone)
# using TPUs, even though they're slower to start up, since they kick off downloads
import requests
f = requests.get("https://storage.googleapis.com/patents-public-data/patents.zip")
with open("patents.zip", "wb") as g:
    g.write(f.content)
import zipfile
z = zipfile.ZipFile("patents.zip")
z.extractall("patents")

