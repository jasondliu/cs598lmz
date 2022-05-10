from types import FunctionType
list(FunctionType(lambda x:x,{}, 'func'))
list(FunctionType(lambda x:x,{}, 'func',()))
list(FunctionType(lambda x:x,{}, 'func',(),None))
list(FunctionType(lambda x:x,{}, 'func',(),None,None))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,()))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),""))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),"",()))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),"",(),()))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),"",(),(),""))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),"",(),(),"",()))
list(FunctionType(lambda x:x,{}, 'func',(),None,None,(),"",(),(),"",
