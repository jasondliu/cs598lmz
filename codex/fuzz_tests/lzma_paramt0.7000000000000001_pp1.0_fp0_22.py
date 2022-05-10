from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/home/francois/Documents/workspace/mp3_analysis/data/jazz/mp3/Thelonious Monk - Crepuscule with Nellie.mp3', 'rb').read())

s = "this is a string"

print(s.encode('utf-8').hex())

import hashlib
hashlib.md5(s.encode('utf-8')).digest().hex()

import librosa
y, sr = librosa.load('/home/francois/Documents/workspace/mp3_analysis/data/jazz/mp3/Thelonious Monk - Crepuscule with Nellie.mp3')
y
 
import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(10, 2000)
X[0,:] = X[0,:] * 100
plt.imshow(X, aspect='auto', interpolation='nearest')
plt.show()

import librosa
import librosa.display
y,
