import select
# Test select.select()

# Set up some pipes
rlist, wlist = [], []
for i in range(3):
    r, w = os.pipe()
    rlist.append(r);
    wlist.append(w)

try:
    read, write, exc = select.select(rlist, wlist, [])
finally:
    for f in rlist:
        os.close(f)
    for f in wlist:
        os.close(f)

print("read =", read)
