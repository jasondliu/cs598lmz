import bz2
bz2.decompress(data)

# Compress the data
bz2.compress(data)

# Compress the data and save it to a new file
bz2.compress(data, filename='example.bz2')
```

## Example

```python
import bz2

with open('example.txt', 'rb') as input:
    data = input.read()

with open('example.bz2', 'wb') as output:
    output.write(bz2.compress(data))
```

## Installation

### Requirements

* [Python](https://www.python.org/) 3.5 or newer

### Setup

Install the latest version of `bz2` with [pip](https://pip.pypa.io/en/stable/):

```bash
python3 -m pip install --user bz2
```

### Usage

```python
import bz2
```

## Documentation

### `bz2.decompress(data)`

Decomp
