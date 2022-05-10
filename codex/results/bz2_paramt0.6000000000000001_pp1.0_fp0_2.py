from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/enwiki-latest-pages-articles.xml.bz2', 'rb').read())

# 使用內建的bz2模組
import bz2
bz2.decompress(open('data/enwiki-latest-pages-articles.xml.bz2', 'rb').read())

# 使用bz2file
import bz2file
bz2file.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb').read()

# 使用pandas模組
import pandas as pd
pd.read_csv('data/enwiki-latest-pages-articles.xml.bz2', compression='bz2')

# 使用pyarrow
import pyarrow.parquet as pq
pq.read_table('data/enwiki-latest-pages-articles.xml.bz2', compression='bz2')

# 使用gzip
import gzip

