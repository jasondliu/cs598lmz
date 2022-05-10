import lzma
lzma(0)
lzma()
 
x = lzma()
lzma(100)
lzma()

#sample run
#Value of z is 0
#Value of z is 0
#Value of z is 0
#Value of z is 100


#instance attribute
def lzma(x):
    if x == 0:
        lzma.z = 3
        print(lzma.z)
    else:
        lzma.z += 10
        print(lzma.z)
lzma(0)
lzma()
x = lzma()
lzma(100)
lzma()

#sample run
#3
#3
#3
#13

def lzma(x):
    lzma.z = x
    print(lzma.z)

lzma(0)
lzma(100)
lzma(200)

#sample run
#3
#3
#3

l0 = lzma()
l100 = lzma(100
