import ctypes
ctypes.cast(23, ctypes.py_object)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#%%----------------------------------------------------------------------------------

# 前知识回顾
Memery = {Name:'1024', number:'1234'}

Memery = {'Name':'1024', 'number':'1234'}

Memery['Name'] = '1024'


for key in Memery:
    print(Memery[key])
    print(key)

for key, value in Memery.items():
    print(key)
    print(value)

# 字典推导式
    # 用法与列表推导式相同，但是生成的是字典
new_dict={key:value**2 for (key,value) in Memery.items()}

# 字典的函数操作
#
