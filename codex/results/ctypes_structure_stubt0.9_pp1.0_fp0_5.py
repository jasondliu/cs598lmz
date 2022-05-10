import ctypes

class S(ctypes.Structure):
    x = 0

def foo(obj):
    if not isinstance(obj, ctypes.Structure) or len(obj._fields_) != 1:
        raise AssertionError("not equal")

def main():
    foo(S())
    print 'Done'

main()
</code>
The above gives the following error while compiling with <code>nuitka</code>.
<code>Starting compilation to C++ of .main with Nuitka-0.5.32.2
Traceback (most recent call last):
  File "C:\Python27\Scripts\nuitka-script.py", line 9, in &lt;module&gt;
    load_entry_point('Nuitka==0.5.32.2', 'console_scripts', 'nuitka')()
  File "build\bdist.win32\egg\nuitka\Main.py", line 149, in main
  File "build\bdist.win32\egg\nuitka\Main.py", line 152, in nuitkaMain
  File "build\bdist.win32\egg
