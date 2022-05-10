from lzma import LZMADecompressor
LZMADecompressor()


# In[ ]:


# https://lzma.readthedocs.io/en/latest/api/lzma.html#decompression-example

import gzip
import shutil
with gzip.open('C:\\Users\\User\\Desktop\\coffee_shop_prediction_deployment\\coffee_shop_prediction_model_deployment.gz', 'rb') as f_in:
    with open('C:\\Users\\User\\Desktop\\coffee_shop_prediction_deployment\\coffee_shop_prediction_model_deployment', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
