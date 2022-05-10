import bz2
# Test BZ2Decompressor

with open("sample.bz2", "rb") as src:
    decompressor = bz2.BZ2Decompressor()
    with open("sample.out", "wb") as dst:
        for block in iter(lambda: src.read(100 * 1024), b''):
            out = decompressor.decompress(block)
            if out:
                dst.write(out)
 
print(decompressor.unused_data)

print(open("sample.bz2", "rb").read())

print(open("sample.out", "rb").read())

# assert open("sample.out", "rb").read() == bz2.BZ2File("sample.bz2").read()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.cluster import AgglomerativeClustering
from sklearn.mixture import GaussianMixture
