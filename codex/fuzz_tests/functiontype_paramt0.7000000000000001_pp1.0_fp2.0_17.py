from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

def size_of_object(obj):
  # https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
  import sys
  return sys.getsizeof(obj)

def get_object_size(obj):
  """
  Returns the approximate memory footprint an object and all of its contents.

  Automatically finds the contents of the following builtin containers and
  their subclasses:  tuple, list, deque, dict, set and frozenset.
  To search other containers, add handlers to iterate over their contents:

      handlers = {SomeContainerClass: iter,
                  OtherContainerClass: OtherContainerClass.get_elements}

  """
  from collections import deque
  from sys import getsizeof, stderr
  from itertools import chain
  from collections import deque
  from sys import getsizeof, stderr
  from itertools import chain
  from reprlib import repr

  dict
