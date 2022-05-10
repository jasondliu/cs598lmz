import select
# Test select.select():
r = select.select([sys.stdin], [], [], 10)
if r[0]:
    print("Got input!")
else:
    print("No input!")

# Test select.poll():
p = select.poll()
p.register(sys.stdin)
r = p.poll(10)
