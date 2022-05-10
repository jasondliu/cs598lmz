fn = lambda: None
gi = (i for i in ())
fn.__code__ = iter(gi)
fn()

def gen(x):
    yield x
    x += 1
    yield x
    del x
    yield x

gen_inst = gen(7)

print(gen_inst.gi_code)
print(gen_inst.gi_frame is None)
print(gen_inst.gi_running)
print(gen_inst.gi_frame.f_lasti)
gen_inst.send(None)
print(gen_inst.gi_frame is None)
print(gen_inst.gi_code.co_freevars)
gen_inst.send(None)
print(gen_inst.gi_frame is None)
#gen_inst.send(None)

def gen2(x):
    y = yield x
    print("A", y)
    yield x + 1
    y = yield x + 2
    del x
    yield
    print("B", y)

g2 = gen2(10)
print(g2)
print("1", next(g2))
print("2", g2.send("
