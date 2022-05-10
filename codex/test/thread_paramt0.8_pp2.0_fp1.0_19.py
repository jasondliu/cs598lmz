import sys, threading
threading.Thread(target=lambda: sys.stderr.write(input()+'\n')).start()
a=[]
n=int(input())
for i in range (2*n):
    a.append(int(input()))
#print(a)
b=''
e=0
r=[0]*n
for i in range (n):
    if a[i]==a[i+n]:
        b=b+'0'
        r[i]=0
    else:
        b=b+'1'
        r[i]=1
#print(r)
b=b[::-1]
#print(b)
s=0
for i in range (n):
    s=s+r[i]*(2**(i))
#print(s)
for i in range (n):
    for j in range (n):
        if (a[i+n]==a[j]):
            e=j
        #print(e, end =' ')
    print(s^e, end =' ')
    e=0
