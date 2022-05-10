import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong

def main():
    s = S()
    s.x = 0x123456789abcdef0
    print s.x

if __name__ == '__main__':
    main()
</code>
I'm running Windows 7 SP1, Python 2.7.3 32-bit, and clang 3.3. I'm compiling it with <code>clang -c -m32 -fno-use-cxa-atexit -O2 -o test.o test.c</code>.
Is there a way I can force it to compile to the same executable (or one that behaves the same way)?


A:

It turns out that this is a bug in the version I'm using (3.3). It works fine in 3.4. I obtained 3.4 from this PPA.

