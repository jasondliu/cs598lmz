import io
# Test io.RawIOBase
urllib.request.urlopen("http://google.com", timeout=1)
import builtins
builtins.open = io.RawIOBase
# returns nothing, but test if it crashes
builtins.open(__file__)
def f(the_file):
    data = the_file.read(12)
    contents = the_file.read()
f(urllib.request.urlopen("http://google.com", timeout=1))
f(open(__file__))

# Test str.format
builtins.str.format
str.format("{{{} total}}", 42)
str.format("{{{} total}}").format(42)
str.format("{total}", total=42)
str.format("{total}").format(total="answer")
str.format("{0}", "answer")
str.format("{0.length}", "answer")
str.format("{0[1]}{1}", "answer", 42)
str.format("{x}", x="answer")
str.format("{{}}", 42)

