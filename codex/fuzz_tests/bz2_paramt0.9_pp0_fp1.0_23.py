from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(pickle.load(bz2.BZ2File('./depth.pkl.bz2', 'r')))
# Decompress the pickle file
!bunzip2 -k ./depth.pkl.bz2
import pickle
with open('./depth.pkl','rb') as f:
    data = pickle.load(f,encoding='latin1')
data

data = pickle.load(f,encoding='latin1')

# Remove the decompressed file after loading the pickle file
import os
os.remove('./depth.pkl')
import pandas as pd
data.shape
type(data[0,0])
data[:,0]
data.columns[1:]
data.columns[1:]
data_df = pd.DataFrame(data,columns=['mjd','airmass','skybrightness','sky_sd','sky_bkgd','telescope_bkgd','exptime','airmass'])
data_df.head()
data_df.head
