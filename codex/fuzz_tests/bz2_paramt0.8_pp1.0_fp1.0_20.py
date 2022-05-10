from bz2 import BZ2Decompressor
BZ2Decompressor

from multiprocessing import Pipe
Pipe

from sklearn.manifold import TSNE
TSNE

from sklearn.manifold import Isomap
Isomap

from sklearn.model_selection import train_test_split
train_test_split

from sklearn.neighbors import KNeighborsClassifier
KNeighborsClassifier

from sklearn.decomposition import PCA
PCA

from sklearn.decomposition import IncrementalPCA
IncrementalPCA
</code>
Each package can be imported without errors but when I import the whole file (or even when I press <code>Run All</code>), I get the following error:
<code>Traceback (most recent call last):
File "C:\Users\Piotr\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py", line 3326, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File "&lt;ipython-input-1-9fa5d5f3
