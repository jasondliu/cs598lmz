from lzma import LZMADecompressor
LZMADecompressor

In [26]: from functools import wraps
    ...: from six import string_types
    ...: from .models.utils import Vocab
    ...: from .iterators import LazyIter, LazyIndexedCorpus
    ...: from .iterator_utils import (smart_ropen, get_titles,
    ...:                             APPLY_FIRST_SENTENCE, APPLY_WHOLE_SENTENCE,
    ...:                             APPLY_CONTINUE_LINES, APPLY_WHOLE_LINE)
    ...: 

In [26]: 
</code>
I even tried installing earlier version of gensim like this
<code>pip install gensim==3.8.1
</code>
However still the same error


A:

Have you tried to manually install lzma package?
<code>pip install lzma
</code>
It appears to be installed with gensim==3.8.1 but if there is some error in your disk you may need to install it manually.

