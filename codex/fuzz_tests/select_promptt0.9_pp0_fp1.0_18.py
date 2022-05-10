import select
# Test select.select
# Watch for readability and writability of sys.stdin and sys.stdout

print "Start of select"
print "stdin", select.select([sys.stdin],[],[])
print "stdout", select.select([],[sys.stdout],[])
print "stdin+stdout", select.select([sys.stdin],[sys.stdout],[])
print "End of select"

time.sleep(1)
print "End of sleep"
time.sleep(2)
print "End of sleep"

# Test select.poll 
# Poll for readability of sys.stdin

p = select.poll()
p.register(sys.stdin,select.POLLIN)
print "Start of poll"
for i in range(10):
	print p.poll(1000)
	time.sleep(1)
	if i==5:
		print p.poll(1000)
print "End of poll"

# Test select's error conditions

try:
	select.select([], [], [], "spam")
	print "No TypeError"
