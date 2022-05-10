import select
# Test select.select function
# [timeout] = 0: don't wait
# [timeout] = negative: wait forever
# [timeout] = positive: socket is set after [timeout] sec
# In which condition does the socket become set
S, O, E = select.select(
    [sys.stdin], [], [], 0.0
)

# Check if stdin is set
if S:
# Print the content of stdin
    i = sys.stdin.readline()
    print(i)

# The above codes can't complete select.select()
# The stdin is never set
# Must use the following code
#
# cat [anyfile] | python [this_program]
# then the stdin is set and the content of [anyfile] is printed on the screen

#
# select.poll()
# The [select.poll()] function is similar to [select.select()]
# It also has 3 arguments. The first is an array of file descriptors
# The second and third arguments are null lists
# The [select.poll()] function returns a poll object
# We can use the
