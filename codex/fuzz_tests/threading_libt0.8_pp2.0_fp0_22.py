import threading
threading.stack_size(2**27)
import sys
#sys.setrecursionlimit(10**7)
sys.setrecursionlimit(10**5)

def binomialCoeff(n , k): 
    res = 1
    if (k > n - k): 
        k = n - k 
    for i in range(0 , k): 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 

def pascalTriangle(n , r): 
    return binomialCoeff(n , r) 

def main():
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    result = pascalTriangle(n , k)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

threading.Thread(target=
