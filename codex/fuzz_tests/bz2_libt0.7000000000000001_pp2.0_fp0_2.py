import bz2
bz2.BZ2File('datasets/dutch_speech_mfcc.bz2').read()

# with bz2.BZ2File('datasets/dutch_speech_mfcc.bz2','r') as bzip_file:
#     for line in bzip_file:
#         print(line)

# with open('datasets/dutch_speech_mfcc.bz2') as f:
#     for line in f:
#         print(line)

# read in the data
data = np.frombuffer(bz2.BZ2File('datasets/dutch_speech_mfcc.bz2').read(), dtype=np.float32)
print(data)
print(data.shape)

# reshape the data into a matrix where each row is a vector of 13 MFCC coefficients
data = np.reshape(data, (-1, 13))
print(data.shape)
