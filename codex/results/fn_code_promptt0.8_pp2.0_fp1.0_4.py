fn = lambda: None
# Test fn.__code__.co_flags & CO_GENERATOR
# Set to False if generator functions are not supported
# Set to True if generator functions are supported
fn.__code__.co_flags & CO_GENERATOR

# Generators
# Using a for loop to run each iteration of a generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

c = countdown(3)
print(c)

for i in c:
    print(i)

# Implementing a generator as an iterable class
class LineHistory:
    def __init__(self, lines):
        self.lines = lines
        self.history = []

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    
    def clear(self):
        self.history.clear()

with open('input.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        if 'python' in line:
            #
