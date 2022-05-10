import types
types.IntType == type(1)
types.StringType == type('1')
types.DictionaryType == type(dict())
types.ListType == type([])
types.StringType == type(1)

print(type(1) == types.IntType)
print(type('1') == types.StringType)
print(type(dict()) == types.DictionaryType)
print(type([]) == types.ListType)
print(type(1) == types.StringType)
