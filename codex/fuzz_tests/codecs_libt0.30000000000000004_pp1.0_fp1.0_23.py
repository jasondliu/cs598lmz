import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from datetime import datetime

#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#import matplotlib.cbook as cbook
#import matplotlib.ticker as ticker
#from datetime import datetime

#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA

#from sklearn.cluster import KMeans
#from sklearn.mixture import GaussianMixture

#from sklearn.metrics import silhouette_samples, silhouette_score

#from sklearn.manifold import TSNE

#from sklearn
