import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Load the Pandas libraries with alias 'pd'
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("C:/Users/jeanbaptiste/bureau/challenge_video_audio/data/interim/data_with_features.csv", sep=';')
# Preview the first 5 lines of the loaded data
print(data.head())

#data.to_csv('C:/Users/jeanbaptiste/bureau/challenge_video_audio/data/interim/data_with_features.csv', sep=';')

#data = pd.read_csv("C:/Users/jeanbaptiste/bureau/challenge_video_audio/data/interim/data_with_features.csv", sep=';')
#print
