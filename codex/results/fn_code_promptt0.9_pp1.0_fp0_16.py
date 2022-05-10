fn = lambda: None
# Test fn.__code__.co_names is a copy of fn.__code__.co_varnames
def f1(a, b, c, d, e=1, f=2, g=3, h=4, i=5, j=6, k=7, l=8, m=9, n=10, o=11, p=12, q=13, r=14, s=15, t=16, u=17, v=18, w=19, x=20, y=21, z=22, aa=23, bb=24, cc=25, dd=26, ee=27, ff=28, gg=29, hh=30): pass
fn = f1
names = set(fn.__code__.co_names)
names = names - set(fn.__code__.co_varnames[:fn.__code__.co_argcount])
names = names - set(map(lambda arg: arg[0] if arg else '', fn.__defaults__))
assert names == {'basestring', 'bool', 'tuple'}
