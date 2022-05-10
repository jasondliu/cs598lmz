import ctypes

class S(ctypes.Structure):
    x = 1

def get_arg():
    return S()

def run(c):
    for i in range(10000):
        x = c.x
    return x

def main():
    c = get_arg()
    return run(c)

if __name__ == "__main__":
    for i in range(3):
        main()
