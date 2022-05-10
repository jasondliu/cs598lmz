from _struct import Struct
s = Struct.__new__(Struct)
Struct._map_ = map_
```

### Specifying Struct Names

The Struct class supports named structs by passing keyword arguments.

```python
s = Struct(name = 'test', format = '=BBH')
print s.name
s = Struct(format = '=BBH')
s.name = 'test'
print s.name
```

### Specifying Struct Attributes

The Struct class supports arbitrary attributes by passing keyword arguments.

```python
s = Struct(blah = 'foo', format = '=BBH')
print s.get('blah')
print s.blah
s.blah = 'boo'
print s.blah
del s.blah
print s.blah
```

### Specifying Struct Methods

The Struct class supports arbitrary methods by passing keyword arguments.

```python
s = Struct(blah = lambda s: 0, format = '=BBH')
print s.blah()
s.blah = lambda s: 1
print s.blah()
```

### Using Structs for
