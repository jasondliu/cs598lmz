import gc, weakref
from collections import defaultdict
from rpython.annotator.model import SomeInteger
from rpython.annotator.model import SomeString
from rpython.annotator.model import SomeChar
from rpython.annotator.model import SomeObject
from rpython.annotator.model import SomeTuple
from rpython.annotator.model import SomeList
from rpython.annotator.model import SomeDict
from rpython.annotator.model import SomeSet
from rpython.annotator.model import SomeInstance
from rpython.annotator.model import SomeBuiltin
from rpython.annotator.model import SomeBuiltinMethod
from rpython.annotator.model import SomePBC
from rpython.annotator.model import SomeExternalObject
from rpython.annotator.model import SomeInterplevelHelper
from rpython.annotator.model import SomeWeakRef
from rpython.annotator.model import SomeImpossibleValue
from rpython.annotator.model import SomeAddress
from rpython.annotator.model import SomeIterator
from rpython.annotator.model import SomeOrderedDict
from rpython.
