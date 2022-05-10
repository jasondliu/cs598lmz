from lzma import LZMADecompressor
LZMADecompressor()

# Load pickled data
import pickle
pickle.load(open('small_train_triplets.txt','rb'))

# Load data from a csv file
# header = None specifies that the first line in the file contains the column names
import pandas as pd
pd.read_csv('train_triplets.txt', sep='\t', header=None)
pd.read_csv('sample_submission_triplets.txt', sep='\t', header=None)
train_triplets = pd.read_csv('train_triplets.txt', sep='\t', header=None)
train_triplets.columns = ['user_id', 'song_id', 'play_count']

# Read a subset of the columns
import pandas as pd
msd_metadata = pd.read_csv('taste_profile_song_to_tracks.txt',sep='\t', header=None)
msd_metadata.columns = ['song_id','track_id','artist_name','title']
msd_metadata[['song_id','track
