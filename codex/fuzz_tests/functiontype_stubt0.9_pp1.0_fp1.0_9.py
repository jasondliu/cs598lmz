from types import FunctionType
a = (x for x in [1])
#b = (x for x in [1])
a = list(a)


#a = (x for x in range(1,100))
#b = list(a)
#b = reduce(lambda x,y:x+y,b)
#b = reduce(lambda x,y:x+y,list(b),1)

# ############测试是否是某种类型  isinstance(object, classinfo) ##############
b = isinstance(a,Iterator)

'''
zip():接受任意多个序列作为参数，返回一个tuple列表
zip(a,b)
'''
a = [1,2,3]
b = [4,5,6]
z = list(zip(a,b))
z = zip(a,b)
a = z
'''
reversed ():返回一个反转的迭
