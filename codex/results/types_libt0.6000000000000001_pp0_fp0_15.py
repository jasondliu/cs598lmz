import types
types.FunctionType

# 判断变量是否是某个类型
isinstance([1,2,3],(list,tuple))
isinstance('abc',(str,unicode))

# 判断变量是否是某个类型中的一种
type('abc') == types.StringType
type('abc') == types.UnicodeType

# 判断变量是否是某种类型
isinstance('abc',types.StringTypes)

# 根据类型字符串动态创建类
def fn(self,name='World'):
	print('Hello,%s.' % name)
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()

# 高阶函数
# 把函
