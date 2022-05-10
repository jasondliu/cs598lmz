from types import FunctionType
list(FunctionType(1,2))

# This is the listcomp version
[FunctionType(1,2)]

# This is the generator version
(FunctionType(1,2),)

# This is the map version
map(FunctionType, [1],[2])

# This is the filter version
filter(None, [FunctionType(1,2)])

# This is the reduce version
(lambda x,y: x + y)(FunctionType(1,2))

# This is the anything but listcomp version
{FunctionType(1,2)}
```

## Installation

```
pip install listcomp-detector
```

## Usage

```
listcomp-detector check --help
```

```
Usage: listcomp-detector check [OPTIONS]

  Checks files for list comprehensions and suggests alternatives.

  The following options can be used to improve the results:

  --lines INTEGER  The maximum number of lines a list comprehension can be.
  --columns INTEGER  The maximum number of columns a list comprehension can
                     be.

