import select
# Test select.select
t = 0.5
r,w,e = select.select( [], [], [], t )
print repr(r),repr(w),repr(e)
