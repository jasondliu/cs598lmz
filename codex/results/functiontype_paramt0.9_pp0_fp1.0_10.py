from types import FunctionType
list(FunctionType() called)
```

Usage
-----

### Installing

```shell
git clone https://github.com/stesth/functional
```

```python
from functional import *
```

Or to use it without the * you can access functions like so:

```py
from operational import operational
query = operational('query_function')
```

### Usage

Documentation can be viewed from the REPL:

```py
help(function)
```

or in the code:

```py
import functional
print(functional.doc_strings)
```

### First

##### List version

```py
first(l)(n)
```

##### String version

```py
first(l)(n)
```

##### Omitting the first argument and using the default len (list and string)

```py
first(l) == first(l)(len(l))
```

### Last

##### List version

```py
last(l)(n)
```
