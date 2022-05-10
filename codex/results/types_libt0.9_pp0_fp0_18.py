import types
types.__all__ += ['UnicodeType','DictType','ListType','FloatType','UnicodeType','StringTypes']
# now we can do something like:
# >>> import types
# >>> types.IntType()
# The types that are used are:
# datetime.time
# types.BooleanType
# datetime.date
# types.IntType
# datetime.timedelta
# types.DictType
# NoneType
# types.FloatType
# list
# types.ListType
# str
# types.StringTypes
# tuple
# types.UnicodeType

# BEGIN new design! (new design is not in here)
# END new design! (new design is not in here)
    
def toJSON( self, encode_datetime_to_str=False, *args, **kwargs ):
    """
    For now this will only encode the basic types that are supported by json.
    In other words, only the list, dict, string and number types. 
    
    For example, dates will not be encoded. Instead,  you can use xml. To
