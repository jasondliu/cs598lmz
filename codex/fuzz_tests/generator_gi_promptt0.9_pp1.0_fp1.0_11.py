gi = (i for i in ())
# Test gi.gi_code.
try:
	print(gi)
except TypeError:
	print("SKIP")
	raise SystemExit
for i in range(5):
	print(gi)
print(list(gi.gi_code.co_varnames))
gj = {i: i for i in range(5)}
# Test gj.gi_base
try:
	print(gj)
except TypeError:
	print("SKIP")
	raise SystemExit
for i in range(5):
	print(gj)
print(list(gj.gi_base))
