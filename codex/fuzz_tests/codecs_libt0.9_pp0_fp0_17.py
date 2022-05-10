import codecs
codecs.encode(text, 'rot_13');
```
python does all the byte manipulation for you.

* * * *

If you need to use an encoding
```python
codecs.open(file_name,mode,encoding='utf-8',errors='strict',buffering=1);
```

**call codecs.open**
- instead of open
- if you need to read/write non-unicode text files

* * * *

**The standard open function decodes the bytes data for you**
```python
with open('data/sample-1.json','r',encoding='utf-8') as f:
	data = json.loads(f.read());
```

```python
#encoding is the default, to tell you the data is unicode

with codecs.open('data/sample-1.json','r',encoding='utf-8') as f:
	data = json.loads(f.read());
```
using codecs gives you an extra error checking

**Example**
```python
import codec
