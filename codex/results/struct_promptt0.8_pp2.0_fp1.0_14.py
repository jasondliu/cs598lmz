import _struct
# Test _struct.Struct
__test__ = {'API_HELPERS': """
>>> import sys
>>> import _struct
>>> class S(_struct.Struct):
>>>     format = 'h l f'
>>> s = S('test',1,2)
>>> s.pack(1,2,3.5)
b't\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x02\\x00\\x00\\x00(B\\x99@'
>>> s.pack_into(1,2,3.5) # test default-offset functionality
>>> s.unpack(s.pack(1,2,3.5))
(1, 2, 3.5)
>>> s.unpack_from(s.pack(1,2,3.5), 2)
(2, 3.5)

# Issue 4979: struct subclasses with explicit __format__ and __sizes__
# should fail early
>>> class S(_struct.Struct):
>>>     __format__ = 'h l f'
>>>     __
