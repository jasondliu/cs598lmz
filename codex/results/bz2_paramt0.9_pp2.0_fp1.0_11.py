from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(Zzw.wave_bytes)

s2 = ipd.Audio(Zzw.wave_bytes)
s2

with open('my_audio.bz2', 'wb') as f:
    f.write(Zzw.wave_bytes)

glob('*.bz2')

#
from IPython.display import Audio , display
from IPython import get_ipython
from numpy import *
from scipy.io import wavfile
from bz2 import BZ2Decompressor
import IPython.display as ipd
from glob import glob
from sklearn.metrics import confusion_matrix,accuracy_score
from scipy.spatial.distance import cdist
from matplotlib.pyplot import *
from fastdtw import fastdtw
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split


s1 = ipd.Audio(glob('./?*')[0])
s2 = ipd.Audio
