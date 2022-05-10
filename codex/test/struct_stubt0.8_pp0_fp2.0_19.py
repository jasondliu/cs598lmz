from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('__doc__', '''Compiled struct pattern.

Used to create compiled struct objects which can be used as follows:

    >>> from _struct import Struct
    >>> st = Struct('i?f')
    >>> s = st.pack(1, 0, 2.5)
    >>> st.unpack(s)
    (1, False, 2.5)

For more information regarding the struct standard see
https://docs.python.org/library/struct.html
''')
