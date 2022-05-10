import types
types.MethodType(lambda self, x: 1, None, BaseProtocol)

"""
[ERROR] /usr/lib/python3.7/asyncio/tasks.py:547:
  'type' object is not subscriptable
  def first_completed(self, fs: Iterable[Future]) -> Future:
"""
type
first_completed = None
BaseProtocol[type]


