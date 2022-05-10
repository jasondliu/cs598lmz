from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# doctest: +ELLIPSIS
[1, 2, 3]

# doctest: +ELLIPSIS
[1, 2, ...]

# doctest: +ELLIPSIS
[1, ..., 3]

# doctest: +ELLIPSIS
[1, 2, ..., 3]

# doctest: +ELLIPSIS
[1, 2, 3, ...]

# doctest: +ELLIPSIS
[..., 1, 2, 3]

# doctest: +ELLIPSIS
[..., 1, 2, 3, ...]

# doctest: +ELLIPSIS
[1, 2, ..., 3, ...]

# doctest: +ELLIPSIS
[1, ..., 3, ...]

# doctest: +ELLIPSIS
[..., 1, ..., 3]

# doctest: +ELLIPSIS
[..., 1, ..., 3, ...]

# doctest: +ELLIPSIS
[..., 1, 2, ..., 3]

