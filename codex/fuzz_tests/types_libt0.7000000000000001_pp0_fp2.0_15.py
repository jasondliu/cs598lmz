import types
types.MethodType(myMethod, myInst)

del myInst.myMethod

myInst.myMethod(2)
