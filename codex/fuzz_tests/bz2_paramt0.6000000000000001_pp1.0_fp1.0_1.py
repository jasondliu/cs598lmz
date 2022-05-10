from bz2 import BZ2Decompressor
BZ2Decompressor().decompress( open( '../data/data.json.bz2', 'rb' ).read())

# Using the requests library
import requests
r = requests.get( 'https://github.com/prabhuSub/data-scientist-roadmap/raw/master/data/data.json.bz2' )
BZ2Decompressor().decompress(r.content)

# Using pandas
import pandas as pd
df = pd.read_json('../data/data.json.bz2', lines=True)
df.head()

# Using gzip
import gzip
import json
json.loads(gzip.decompress( open( '../data/data.json.gz', 'rb' ).read()))

# Using the requests library
import requests
r = requests.get( 'https://github.com/prabhuSub/data-scientist-roadmap/raw/master/data/data.json.gz' )
json.loads(gzip.decompress(r.content))

# Using pandas
import pandas
