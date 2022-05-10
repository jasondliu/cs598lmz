import select
# Test select.select()

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Decorator to measure the time of a function

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print('{} took {} seconds'.format(func.__name__, (end-start)))
        return result
    return wrapper

@time_it
def foo():
    print('in foo()')

foo()

# Decorator to add logging to a function

def log_it(func):
    def wrapper(*args, **kwargs):
        log_string = func.__name__ + " was called"
        print(log_string)
        return func(*args, **kwargs)
    return wrapper

@log_it
def foo():
    print
