import types
# Test types.FunctionType()
def show(num):
    print(num)
    
print(type(show))#<class 'function'>
print(type(show)==types.FunctionType)#True
# Test types.LambdaType()
myLambda = lambda x:x+1
print(type(myLambda))#<class 'function'>
print(type(myLambda)==types.LambdaType)#True
# Test types.GeneratorType()
def myGen():
    yield 1
    yield 2
    
def f(num):
    num = yield num
    yield num+1
    
gen = myGen()
print(type(gen))#<class 'generator'>
print(type(gen)==types.GeneratorType)#True
# Test types.CodeType()
# 编译
import ast
# 编译体
import codeop
# 代码对象
import dis
# 标准输入/输出/错误
import sys

