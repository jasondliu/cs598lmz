import types
types.new_class(cls_name,bases,dict)

# OR
class NewCls(object):
    """docstring for NewCls"""
    def __init__(self, arg):
        super(NewCls, self).__init__()
        self.arg = arg
basecls=type(object)
NewCls=type('NewCls',(basecls,),{'x':0,'y':0}) #NewCls is <class 'type'>
print(type(NewCl
