import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'
b = fun
b()

c = lambda: 'hi'
c()
</code>
И на выходе получаю
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
Подскажите как правильно настроить тип возвращаемого значения, чтобы приведенный код работал.


A:

На выходе получаю:
<code>c()
</code>
<blockquote>
<p>TypeError: 'CFUNCTYPE' object is not callable</p>
</blockquote>
Пробле
