from types import FunctionType
list(FunctionType(c,globals(),'test')())

# eval和exec
# eval会执行字符串形式的python表达式，并返回表达式的结果
eval('3*2')
# exec会执行字符串形式的python代码，不返回结果
exec('print(3)')
print(exec('3*2'))
print(eval('print(3)'))

# python2中的eval和exec可以直接运行代码
# python3中的eval和exec只能运行表达式，无法运行代码
# 要运行代码，必须带上最后一个参数
