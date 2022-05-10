import types
types.ModuleType('test_io')
import test_io
test_io.test(matvec_petsc)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        exec(sys.argv[1])
    else:
        from fipy.tests.doctestPlus import _testPlus
        _testPlus()
