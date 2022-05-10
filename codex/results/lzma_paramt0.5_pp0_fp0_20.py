from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# %%
import itertools

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

# %%
from collections import defaultdict

def count_tokens(tokens, n=1):
    counts = defaultdict(lambda: 0)
    for token in tokens:
        counts[token] += 1
    return counts

# %%
def count_ngrams(tokens, n=1):
    counts = defaultdict(lambda: 0)
    for ngram in zip(*[tokens[i:] for i in range(n)]):
        counts[ngram] += 1
    return counts

# %%
from collections import Counter

def count_tokens(tokens, n=1):
    return Counter(tokens)
