import types
types.MethodType(get_name,s1)

#通过一个实例赋值，其他实例也能调用该方法
s2 = Students()
s2.get_name()


#为Students类动态添加一个方法
def set_name(self,name):
    self.name = name

Students.set_name = set_name

#在类外面调用这个方法
def set_name(self, name):
    self.name = name

Students.set_name = MethodType(set_name,Students)

#在方法里面调用这个方法
s1.set_name("woniu")
s1.get_name()
s2.get_name()


#在类外面赋值,
