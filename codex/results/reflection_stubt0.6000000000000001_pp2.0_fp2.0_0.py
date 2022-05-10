fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# 上のコードは実行時エラーになる

# 同じようなことをやってみる。
class A:
    def __init__(self):
        pass
    def __code__(self):
        return self

a = A()
a.co_argcount = 0
a.co_consts = ()
a.co_filename = ''
a.co_firstlineno = 0
a.co_flags = 0
a.co_lnotab = b''
a.co_name = ''
a.co_names = ()
a.co_nlocals = 0
a.co_stacksize = 0
a.co_varnames = ()

# 無事に exec することができた。
exec(a)

# これによって、コードオブジェクトの一部を書き換えることができる。
def f():
