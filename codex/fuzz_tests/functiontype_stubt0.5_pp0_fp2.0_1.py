from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(FunctionType))
print(type(lambda x:x+1))
print(type(type(lambda x:x+1)))
print(type(type(type(lambda x:x+1))))
print(type(type(type(type(lambda x:x+1)))))
print(type(type(type(type(type(lambda x:x+1))))))
print(type(type(type(type(type(type(lambda x:x+1)))))))
print(type(type(type(type(type(type(type(lambda x:x+1))))))))
print(type(type(type(type(type(type(type(type(lambda x:x+1)))))))))
print(type(type(type(type(type(type(type(type(type(lambda x:x+1))))))))))
print(type(type(type(type(type(type(type(type(type(type(lambda x:x+1)))))))))))
print(type(type(type(type(type(type(
