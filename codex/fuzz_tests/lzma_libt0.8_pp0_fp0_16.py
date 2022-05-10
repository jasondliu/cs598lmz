import lzma
lzma.open("data/myfile.xz")

import pickle
_pickle = pickle.load(open("data/myfile.pickle", "rb"))

import tarfile
with tarfile.open("data/tarfile.tar.gz", "r:gz") as t:
    t.extractall("data/output")

import zipfile
zipfile.ZipFile("data/myzipfile.zip").extractall("data/output")
```



#### Classificação
```python
# sklearn - Machine Learning
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

# Aprendizado supervisionado
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
digits.data[-1]
clf.predict(digits.data[-1:])
```



#### NLP
```python
