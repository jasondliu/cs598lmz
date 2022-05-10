from types import FunctionType
a = (x for x in [1])
b = a.gi_frame.f_lasti
c = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals)
d = c(*a.gi_frame.f_locals)
print d.next()
print a.next()
print d.next()
print a.next()
</code>
I realise that this code is not general and has a certain amount of unpleasantness to it (it also has some missing functionality).  It's also not the correct solution (it doesn't create a proper bound method, so you can't do <code>.next()</code> on the result).  To actually do it right would be quite a lot of work (I've seen the code involved), and it would have to be carefully thought out and written in C, as C is the only way to get truly general results.  It can however be done.

