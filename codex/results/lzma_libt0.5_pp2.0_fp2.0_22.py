import lzma
lzma.LZMAFile(filename)

import bz2
bz2.BZ2File(filename)

import zipfile
zipfile.ZipFile(filename)
```

---

## Pickling

```python
import pickle

data = {'name': 'John', 'age': 25, 'is_student': True}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
```

---

## JSON

```python
import json

data = {'name': 'John', 'age': 25, 'is_student': True}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    data = json.load(f)
```

---

## JSON

```python
import json

data =
