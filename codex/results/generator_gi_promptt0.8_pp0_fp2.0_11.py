gi = (i for i in ())
# Test gi.gi_code.co_filename
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)

# test gi.gi_frame
def add(x, y):
    return x + y
gi = (i for i in (add(1, 2)))
print(gi.gi_frame)

# test gi.gi_running
gi = (i for i in ())
print(gi.gi_running)
gi = (i for i in ())
next(gi)
print(gi.gi_running)

# test gi.send, gi.throw, gi.close
def gen():
    x = 1
    try:
        while True:
            x = yield x
            print('after yield: ', x)
    except GeneratorExit:
        print('except GeneratorExit: ', x)

gi = gen()
g = next(gi)
print(g) # 1
g = gi.send(2)
print(g) # after yield: 2, 2
g = gi.throw(Exception('exception'
