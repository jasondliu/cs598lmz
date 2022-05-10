from types import FunctionType
list(FunctionType(lambda x: x+2,globals()).__closure__)

print(globals())
print(globals().keys())
print(globals().values())
print(globals().items())
print(globals().keys())
print(globals().values())
print(globals().items())

print('*' * 20)
function_1 = Lambda()
function_2 = func_generator(5)

# function_1()
# function_2()
# Point(x=1,y=2)
# my_dic = {'x':1,'y':2}
# Point(**my_dic)
# Point(*my_dic)

# l_1 = [3,5]
# l_2 = [7,12]
# l_3 = [1,11]
# res = list(map(lambda x,y:x+y,l_1,l_2))
# print(res)
#
# res = list(map(lambda x,y:x+y,l_1
