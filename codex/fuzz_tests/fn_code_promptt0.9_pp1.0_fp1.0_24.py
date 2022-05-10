fn = lambda: None
# Test fn.__code__.co_firstlineno.
test.write_test_tool( 'script', dedent('''
from sys import argv
__file__ = argv[1]
l = __file__.__code__.co_firstlineno + 2
if 2 * l != __file__.__code__.co_firstlineno + 4:
    print("this line can not be found")
''') )
test_exp = """\
"""

test.run_scons2(["-f", "SConstruct1", "script", test.workpath("script")],
                stdout=test_exp)

test_exp = """\
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
gcc -o example1.o -c example1.c
gcc -o example2.o -c example2.c
gcc -o example example1.o example2.o
scons: done building targets.
"""

test.run_scons2(["-f", "SConstruct3", "-c"],
