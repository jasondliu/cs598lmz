import select
# Test select.select
r, w, e = select.select( [], [], [], 0 )
print(r, w, e)

r, w, e = select.select( [], [], [], 0.0 )
print(r, w, e)

r, w, e = select.select( [], [], [], 0.01 )
print(r, w, e)

r, w, e = select.select( [], [], [], 0.1 )
print(r, w, e)

r, w, e = select.select( [], [], [], 1.0 )
print(r, w, e)

r, w, e = select.select( [], [], [], 2.0 )
print(r, w, e)

r, w, e = select.select( [], [], [], 3.0 )
print(r, w, e)

r, w, e = select.select( [], [], [], 4.0 )
print(r, w, e)

