import bz2
bz2.BZ2Compressor.compress(b'hello')
bz2.BZ2Compressor.flush()

## rlcompleter
import readline
readline.parse_and_bind('tab: complete')

## pygments
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight
code = """
for i in range(1, 11):
    print("Hello world!")
"""
print(highlight(code, PythonLexer(), TerminalFormatter()))

## tracemalloc
import tracemalloc
tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()
import wasted_memory
x = wasted_memory.run()
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)
