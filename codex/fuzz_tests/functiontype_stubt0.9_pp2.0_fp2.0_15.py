from types import FunctionType
a = (x for x in [1])
b = (1)
c = list(a)

d = {}
def g():
    def h():
        pass

    return h

if __name__ == '__main__':
    import dis
    print(dis.dis(g))
    e = g()
    print(e.__closure__)
