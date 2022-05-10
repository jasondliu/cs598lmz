gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test generator.send()
def gen():
    yield 1
    yield 2
    yield 3

gen1 = gen()
print(gen1.send(None))
print(gen1.send(None))
print(gen1.send(None))

# Test generator.send() with exception
def gen():
    try:
        yield
    except Exception as e:
        print(e)

gen1 = gen()
gen1.send(None)
gen1.send(Exception('test'))

# Test generator.close()
def gen():
    try:
        yield 1
    except GeneratorExit:
        print('closed')

gen1 = gen()
print(gen1.send(None))
gen1.close()

# Test generator.throw()
def gen():
