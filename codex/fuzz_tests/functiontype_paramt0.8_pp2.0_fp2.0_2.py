from types import FunctionType
list(FunctionType(lambda: object(), object))

# ___ is TupleType
tuple.__name__
'object'

# ___ is ListType
list.__name__
'object'

# ___ is DictionaryType
dict.__name__
'object'

# ___ is FileType
open('C:/Users/moment/Desktop/ProgrammingLearning/Python/Modules/Test.txt')

# ___ is IntType
int.__name__
'object'

# ___ is LongType
long.__name__
'object'

# ___ is FloatType
float.__name__
'object'

# ___ is ComplexType
complex.__name__
'object'

# ___ is SliceType
slice(object)

# ___ is XRangeType
xrange(object)

# ___ is EllipsisType
Ellipsis.__name__
'object'

# ___ is StringType
str.__name__
'object'

# ___ is UnicodeType
unicode.__name__
'object'

# ___ is BufferType
buffer(object)

