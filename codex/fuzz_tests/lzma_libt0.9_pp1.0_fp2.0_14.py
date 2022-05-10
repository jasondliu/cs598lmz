import lzma
lzma.open()

print "Entering the matrix..."
import numpy as np

print "Let's make some vectors..."
vec = np.array([1, 2, 3, 4, 5])
print "vec = " + str(vec)

print "Multiplying the vector by -1..."
multiplied = vec * -1
print "multiplied = " + str(multiplied)

print "Let's make a 3x3 matrix of zeros..."
zeros = np.zeros((3, 3))
print "zeros = \n" + str(zeros)

print "Making some random 10x10 matrix..."
rand = np.random.rand(10, 10)
print "rand = \n" + str(rand)

print "Summing the matrix..."
summed = rand.sum()
print "summed = " + str(summed)

print "Reshaping the matrix to size 100..."
size100 = rand.reshape(100, 1)
print "size100 = \n" + str(size100)

print "Let's plot some things!"

