from types import FunctionType
list(FunctionType(lambda x:x**2,globals()) for i in range(4) if FunctionType(lambda x:x**2,globals())%2) 
#square**2
#square**2
#square**2
#square**2
