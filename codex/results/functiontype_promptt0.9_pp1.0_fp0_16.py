import types
# Test types.FunctionType
def vm_fn_2():
    pass
def fn_3():
    def fn_3_1():
        pass
    fn_3_1()
fn_3()
def vm_fn_2(a, kw):
    pass
def fn_3():
    def fn_3_2(a, kw):
        pass
    fn_3_2('a', {})
fn_3()
def fn_3():
    def fn_3_3(a, kw={'a': 1}):
        pass
    fn_3_3('a')
fn_3()
def vm_fn_2(a, *argv, kw, *kwargv):
    pass
def fn_3():
    def fn_3_4(a, *argv, kw, *kwargv):
        pass
    fn_3_4('a', 'b', 'c', d='d')
fn_3()
def fn_3():
    def fn_3_5(a, *argv, kw={'a': 1}, *kw
