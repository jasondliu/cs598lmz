from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(Struct, "s" )
s.unpack( s.pack("jaslkdf") )
```

```python
import _struct
```

```python
_struct.unpack("<s", "jaslkdf")
```

```python
%timeit _struct.unpack("<s", "jaslkdf")
```

```python
_struct.unpack("<ss","jaslkdf")
```

```python
_struct.unpack("<ss","jaslkdf")
```

```python
("jaslkdf")*10
```

```python
%timeit _struct.unpack("<10s","jaslkdf" * 10)
```

```python
%timeit _struct.unpack("<10s","jaslkdf" * 100)
```

```python
%timeit _struct.unpack("<10s","jaslkdf" * 10000)
```

```python
%
