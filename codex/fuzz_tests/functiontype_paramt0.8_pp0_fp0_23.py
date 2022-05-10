from types import FunctionType
list(FunctionType(source, globals(), 'foo')) = [1, 2, 3]
"""
    },
"""
from types import FunctionType
print(FunctionType(source, globals(), 'foo')('abc'))

abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc
"""
    ]

    exec(compile(source, '<unknown>', 'exec'))

    example(source, examples)

    print(FunctionType(source, globals(), 'foo')('abc'))
