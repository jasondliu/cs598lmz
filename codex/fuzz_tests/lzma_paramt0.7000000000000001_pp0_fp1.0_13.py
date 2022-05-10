from lzma import LZMADecompressor
LZMADecompressor().decompress(body)


# %%
def make_n_grams(text, n=1):
    n_grams = []
    for i in range(len(text) - n + 1):
        n_grams.append(text[i:i+n])
    return n_grams


# %%
text = """
コーパスってなに？
"""


# %%
list(set(make_n_grams(text, 1)))


# %%
list(set(make_n_grams(text, 2)))


# %%
list(set(make_n_grams(text, 3)))


# %%
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/prayzzz/user_sim/master/data/sample_data.csv')


# %%
df.head()


# %%
df.groupby('user_id').count()


# %%
df.groupby('user_id')[['item_id']].count()



