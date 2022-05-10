import threading
threading.stack_size(67108864)

def count_down(n):
    while n > 0:
        n -= 1

print('Starting')
count_down(100000000)
print('Done')

# Starting
# Done

# Stack size is 1MB by default
# If you run the code above, you will get a recursion error
# Increase the stack size to 64MB, then it will run

# However, you can use a generator to do this
# You can keep the stack size small
def count_down(n):
    while n > 0:
        yield n
        n -= 1

print('Starting')
for i in count_down(100000000):
    pass
print('Done')

# Starting
# Done

# Use a generator when you're not sure how much memory you're using
# Use a generator when you're not sure how long the loop will take
# Use a generator when you want to pause the loop
# Use a generator when you want to resume the loop
# Use a generator when you want to yield values

# Generator functions
# Generator expressions

#
