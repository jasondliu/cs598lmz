import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('/home/dsc/Data/opentraveldata/optd_airlines.csv.bz2', 'rb') as input:
    with open('/home/dsc/Data/opentraveldata/optd_airlines.csv', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))
 
import pandas as pd
airlines = pd.read_csv('/home/dsc/Data/opentraveldata/optd_airlines.csv', sep='^')
airlines.head()

# Test BZ2File

with bz2.BZ2File('/home/dsc/Data/opentraveldata/optd_airlines.csv.bz2', 'rb') as input, open('/home/dsc/Data/opentraveldata/optd_airlines.csv', 'wb') as output
