import types
# Test types.FunctionType()

def metodoUno():
  print(1)
  
def metodoDos():
  print(2)
  
print(type(metodoUno))
print(type(metodoDos))

print( isinstance(metodoUno() , int) )
print( isinstance(metodoDos() , int) )

# Test type()
print(type(metodoUno) == types.FunctionType)
print(type(metodoDos) == types.FunctionType)

# Test isinstance
print(isinstance(metodoUno, types.FunctionType))
print(isinstance(metodoDos, types.FunctionType))
