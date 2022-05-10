import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Recursive-Fib")    
import time
r = int(input("Ποιο αριθμό θα βρεήτε(ροχαίο)?: "))
z = list(range(0 , r))
tp = time.time()
print("Ο Αριθμός είναι: " + str(fib(r)))
t = time.time() - tp
print(t)

s = str((fib(r)/t))

fp = open('recursive.txt', 'w')
fp.write(s)
fp.close()
