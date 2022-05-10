import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("xero")

cls = lambda: os.system('cls')

def __decorator__(fun):
    def wrapper(*args, **kwargs):
        print(cls())
        return fun(*args, **kwargs)
    return wrapper

def __CORR__(D,A):
    m = list(map(sum, A))
    X = [A[0][i]/m[i] for i in range(len(A[0]))]

    k = len(A)
    n = len(A[0])
    srY = sum(m) / n

    S2y = sum((i - srY)**2 for i in m)
    S2x = sum(j * (i - j) for i, j in zip(X, m))

    r = (S2x / srY) / S2y

    def h(a):
        return a * (1 - a)

    def u(a, b):
        return abs(a - b)

    def mu
