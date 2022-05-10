fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# 沒有參數的 lambda
fn = lambda: None


# lambda 式裡的表示式
fn = lambda: 1 + 1
fn()
fn = lambda: (1 + 1)
fn()
fn = lambda: (1,)
fn()[0]
# 雙層 lambda 式
fn1 = lambda: (lambda: 1)
fn2 = fn1()
fn2()


# 常數依賴於運算式 - 不合法
fn = lambda: m = 1 + 1


# lambda 與星號運算式
def fn(a, *, b):
    pass
fn = lambda a, *, b: None


# lambda 與帶預設值的表達式
def fn(a=None):
    print(a)
fn = lambda a=None: print(a)
fn()


# lambda
