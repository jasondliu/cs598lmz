import select
# Test select.select()

while True:
	print("select")
	readable, writable, errored = select.select( [], [], [] )
	print("readable", readable)
	print("writable", writable)
	print("errored", errored)

# eof
