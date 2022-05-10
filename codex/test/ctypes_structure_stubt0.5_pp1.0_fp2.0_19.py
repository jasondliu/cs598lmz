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
