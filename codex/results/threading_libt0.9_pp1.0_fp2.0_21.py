import threading
threading.stack_size(26820000)
start = time.clock()

def exponentSearch(D,g):
    e=0
    while gcd(e,D)!=1:
        e+=1
    root = 2
    potential = pow(g ,2)
    bound = D
    while potential <= D:
        potential *= 2
        bound *= 2
    while bound >= 2:
        if potential> bound:
            potential= potential * pow(g,2)
            root = 2*root
        else:
            potential *= g
            root *= 1
        bound *= .5
        root =round(root)
    if potential == D:
        return root
    else:
        return false


def factor(n):
    factors = []
    a=math.floor(math.sqrt(n)+1)
    b2=a*a-n
    while b2>0:
        b=math.sqrt(b2)
        if b==round(b):
            factors.append((a-b,a+b))
       
