from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed).decode('utf-8')

# The decompressed data is a pickle:
import pickle
pickle.loads(LZMADecompressor().decompress(compressed))

# The pickle contains a pandas dataframe:
df = pd.read_pickle(LZMADecompressor().decompress(compressed), compression=None)
df.head()

# This data is a snapshot of the Wikipedia edit history for the article on
# Pixar.

# We can use this DataFrame to find the most prolific editors on the page:
df['user'].value_counts().head()

# We can also see the overall trend in the number of edits made to the page:
df.resample('M', on='timestamp').size().plot()

# We can see that the page saw a large increase in edits around the time of the
# release of the movie Cars 2.

# We can use the DataFrame to reconstruct the edit history of the page.  First,
# we need to clean the data a bit:
df['timestamp
