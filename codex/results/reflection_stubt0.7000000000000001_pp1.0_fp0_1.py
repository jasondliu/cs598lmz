fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn)

# 함수 포인터 변수를 함수 포인터 초기화 할 때에는 람다를 이용하여 초기화 하면 된다.
f = lambda x, y: x + y
print(f(10, 20))
