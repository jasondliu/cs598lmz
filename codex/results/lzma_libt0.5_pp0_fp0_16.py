import lzma
lzma.LZMAError: Input format was not recognized
</code>
I've tried to install lzma package, but it was already installed.
My code is:
<code>import pandas as pd
import numpy as np
import lzma

def load_data(path):
    with lzma.open(path, 'rb') as f:
        return pd.read_csv(f)

df = load_data('C:/Users/user/Desktop/data/train.csv.xz')
</code>
What should I do?


A:

The pandas.read_csv() method does not support xz compressed files.
You can use the python-lzma module to decompress the file.
<code>import lzma
import pandas as pd

with lzma.open('sample.csv.xz', 'rb') as f:
    df = pd.read_csv(f)
</code>

