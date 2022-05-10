import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#import pandas as pd
#pd.set_option('expand_frame_repr', False)
#pd.set_option('display.max_rows', 500)

#import numpy as np
#np.set_printoptions(precision=3, suppress=True)

import matplotlib.pyplot as plt
import seaborn as sns
#plt.style.use('ggplot')
#%matplotlib inline
#import plotly.plotly as py
#import plotly.graph_objs as go
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)

#import cufflinks as cf
#cf.go_offline(connected=True)
#cf.set_config_file(theme='white')

#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_
