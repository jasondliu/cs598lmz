import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)
def func(x):
  return x*x+x-2
myfunc = FUNTYPE(func)
numeric.approximate_taylor_polynomial(myfunc, 0.0, 5, 0.1)

"""

#     The approximation is calculated with the help of the error bound
#     <http://mathworld.wolfram.com/LagrangeErrorBound.html>
#
#     .. math::   P_{n}(x) = T_{n}(x) = f(a) + f^{(1)}(a)(x-a) + ... + f^{(n)}(a)(x-a)^n
#
#     where 
#
#     .. math::    |R_{n+1}(x) | = |f(x)-T_{n}(x)| \le (x-a)^{n+1} \frac{M}{(n+1)!}
#     .. math::    R_{n+1}(x) = \sum_{r=n+1}
