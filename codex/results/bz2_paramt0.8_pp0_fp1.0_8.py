from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

```
# Download the data
wget https://xkcd.com/2600/
```

### bz2

```python
import bz2
data = bz2.decompress(bz2_data)
```

```bash
wget https://files.pythonhosted.org/packages/b4/1c/947f0d28fc27e1ec80e07bdf5a5e64c3fa3d3ff8dbb574ac1bff7bcbfa19/bz2file-0.98.tar.gz
tar -zxvf bz2file-0.98.tar.gz
rm -rf bz2file-0.98.tar.gz
cd bz2file-0.98
python setup.py install
```

```bash
cat > /usr/local/bin/bz2cat << EOF
#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3
