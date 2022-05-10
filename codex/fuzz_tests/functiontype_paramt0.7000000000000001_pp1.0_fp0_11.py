from types import FunctionType
list(FunctionType(lambda: 0, {}, "lambda", (0,), 1))

def check_generator(func):
    #@wraps(func)
    def inner(*args, **kwargs):
        gen = func(*args, **kwargs)

        #print func.__name__, gen
        assert isinstance(gen, types.GeneratorType)
        ret = next(gen)

        assert isinstance(ret, types.GeneratorType)
        ret = next(ret)

        assert ret[0] == 'send'
        return gen
    return inner

def check_generator_final(func):
    #@wraps(func)
    def inner(*args, **kwargs):
        gen = func(*args, **kwargs)

        #print func.__name__, gen
        assert isinstance(gen, types.GeneratorType)
        ret = next(gen)

        assert isinstance(ret, types.GeneratorType)
        ret = next(ret)

        assert ret[0] == 'send'
        ret = gen.send(None)
        assert ret
