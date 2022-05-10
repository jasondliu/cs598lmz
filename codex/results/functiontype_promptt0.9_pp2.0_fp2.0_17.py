import types
# Test types.FunctionType
def func(): pass
Test( FunctionType(func), "obj=types.FunctionType" )

# Test kinds
Test( ObjectType, "type(ObjectType)" )
Test( FunctionType, "type(FunctionType)" )
Test( ClassType, "type(ClassType)" )
Test( InstanceType, "type(InstanceType)" )
Test( IntType, "type(IntType)" )
Test( LongType, "type(LongType)" )
Test( FloatType, "type(FloatType)" )
Test( ComplexType, "type(ComplexType)" )
Test( StringType, "type(StringType)" )
Test( UnicodeType, "type(UnicodeType)" )
Test( TupleType, "type(TupleType)" )
Test( ListType, "type(ListType)" )
Test( DictType, "type(DictType)" )
Test( NoneType, "type(NoneType)" )
Test( TypeType, "type(TypeType)" )

unittest.main()
