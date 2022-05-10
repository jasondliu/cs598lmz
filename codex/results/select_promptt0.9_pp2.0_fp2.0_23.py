import select
# Test select.select
r, w, e = select.select( [], [], [], 2)
#try:

print("write_ok:", w)
print("error:", e)
print("read:", r)

#except OSError as e:
#	print(e)
