import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(callback)
del lst
'''
    loop = LLInterpreter(forbidden_operations=llgraph.FORBIDDEN_OPERATIONS)
    try:
        loop.eval_graph(graph, [])
    except LoopLowered:
        pass
    else:
        assert False, "should have failed"
    loop.enable_extra_opcodes()
    loop.eval_graph(graph, [])

def test_callback_and_weakref():
    graph = '''
[p1]
p1 = new_with_vtable(4488)
setfield_gc(p1, 0, descr=valuedescr)
setfield_gc(p1, p1, descr=nextdescr)
jump(p0, p1, p0, p0, p1, descr=targettoken)
'''
    loop = LLInterpreter(forbidden_operations=llgraph.FORBIDDEN_OPERATIONS)
    loop.eval_graph(graph,
