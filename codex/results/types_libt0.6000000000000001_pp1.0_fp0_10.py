import types
types.SimpleNamespace(a=1)

from collections import namedtuple
Test = namedtuple('Test', 'a b c')
Test(a='a', b='b', c='c')

# @dataclass
# class Test:
#     a: str
#     b: str
#     c: str
#
# Test('a', 'b', 'c')

# from dataclasses import dataclass
#
# @dataclass
# class Test:
#     a: str
#     b: str
#     c: str
#
# Test('a', 'b', 'c')
