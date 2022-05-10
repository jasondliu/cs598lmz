import codecs
codecs.register_error('strict', codecs.ignore_errors)

# we don't want to have warnings
import warnings
warnings.filterwarnings('ignore')

# Matplotlib forms basis for visualization in Python
import matplotlib.pyplot as plt

# We will use the Seaborn library
import seaborn as sns
sns.set()

# Graphics in SVG format are more sharp and legible
%config InlineBackend.figure_format = 'svg' 

# Increase the default plot size and set the color scheme
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams['image.cmap'] = 'viridis'

# Увеличим дефолтный размер графиков
from pylab import rcParams
rcParams['figure.figsize'] = 12,9
 
# импорт библиотеки для п
