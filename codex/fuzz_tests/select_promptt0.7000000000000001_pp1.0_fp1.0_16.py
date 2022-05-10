import select
# Test select.select function

read, write, error = select.select([], [], [], 1)
print "Read:", read
print "Write:", write
print "Error:", error

read, write, error = select.select([], [], [], 0)
print "Read:", read
print "Write:", write
print "Error:", error
