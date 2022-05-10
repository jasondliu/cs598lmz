from lzma import LZMADecompressor
LZMADecompressor().decompress(mybz2data)

import bz2
bz2.decompress(mybz2data)
```

**Benchmarking**

```
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
timeit.timeit('"-".join(map(str, range(100)))', number=10000)

timeit.timeit('sum(range(100))', number=10000)
timeit.timeit('sum(x for x in range(100))', number=10000)
```

### The Python Language
* [Official Python Language Reference](https://docs.python.org/3/reference/index.html)
* [Python Quick Reference](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
* [Python for Beginners](https://www.python.org/
