import _struct

print(
    _struct.calcsize(
        [
            ('i', 1, 0),
            ('h', 1, 0),
            ('c', 1, 0),
            ('b', 1, 0),
            ('s', 2, 0),
            ('x', 1, 0),
            ('f', 1, 0),
            ('d', 1, 0),
            ('P', 1, 0),
        ]
    )
)
