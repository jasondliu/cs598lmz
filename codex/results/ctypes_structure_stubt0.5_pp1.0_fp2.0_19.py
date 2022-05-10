import ctypes

class S(ctypes.Structure):
    x = 1

class C(object):
    def __init__(self):
        self.x = 2

def main():
    s = S()
    c = C()
    print(s.x)
    print(c.x)

if __name__ == "__main__":
    main()
</code>
The output is:
<code>1
2
</code>
What I don't understand is why is the output 1 and not 2? Why does the <code>__init__</code> method of the C class not get called when I create an instance of the S class?

