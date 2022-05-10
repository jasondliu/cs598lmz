from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("> i")
s.unpack(buffer("\x00\x00\x00\x0b", 4))
# (11,)
```

The struct module _is_ pure Python, and its performance is close to the actual
CPython implementation.

```
python3 -m timeit -s 'from _struct import Struct; s = Struct("<i"); b = b"\x00\x00\x00\x00"' 's.unpack(b)'
1000000 loops, best of 3: 0.524 usec per loop
```

## Installation

```bash
pip3 install --user micropython-struct
```

## License

Licensed under the terms of the [MIT License](/LICENSE).
