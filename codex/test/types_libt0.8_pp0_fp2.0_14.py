import types
types.ModuleType

class TestError(Exception):
    pass

def bla(x):
    class TestClass(object):
        pass
    raise TestError('bla')

def get_error():
    def nested(x):
        def nested(x):
            def nested(x):
                def nested(x):
                    def nested(x):
                        def nested(x):
                            bla(x)
                        nested(x)
                    nested(x)
                nested(x)
            nested(x)
        nested(x)
    nested(x)

