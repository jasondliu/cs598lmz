gi = (i for i in ())
# Test gi.gi_code is None
gj = (i for i in ())
# Test gj.gi_code is not None


#Test
for i in range(3):
    print(next(gi))
    print(next(gj))


def yf(n):
    return n ** 2 + 1

ti1 = timeit.Timer("f1(x)", "from __main__ import f1, x")
# ti has a timeit method timer.timeit(1) to 
# return the execution time in seconds
print( ti1.timeit()) # perform 1000 times, return time per time in second

popt, pcov = curve_fit(yf, tlist, alist) # find fit in y = a*x+b
print popt, pcov;
measure_time()


def g(x):
    next(x)

ti = timeit.Timer("g(x)", "from __main__ import g, x")
print(ti.timeit()) # perform 100000 times, return time per time in second


ti = timeit.Timer("x=(x for
