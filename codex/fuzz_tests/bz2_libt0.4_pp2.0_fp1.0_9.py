import bz2
bz2.BZ2File('../data/train.ft.txt.bz2').readline()

# read the entire file into a Python array
with bz2.BZ2File('../data/train.ft.txt.bz2') as f:
    data = f.readlines()

# each line is a separate JSON object
data[:1]

# convert it into a list of JSON objects
import json
data = [json.loads(line) for line in data]

data[:1]

# the result is a list of lists
data[0]

# we can normalize it into a DataFrame
import pandas as pd
df = pd.DataFrame(data)
df.head()

# how many reviews are positive vs. negative?
df['review'].str.contains('good').value_counts()

# define a function that accepts text and returns the polarity
def determine_polarity(text):
    return text.str.contains('good').value_counts()

# define a function that accepts text and returns the pol
