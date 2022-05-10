import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
'''

# Python3 program to generate a 
# random function which generates 
# int point in double list 

import random 

def generateRandomPoint(rangeInt): 
  
    # Generate random points 
    x = random.random() * rangeInt 
    y = random.random() * rangeInt 
  
    # Return as a list 
    return [x, y] 
  
# Driver code 
rangeInt = 100

# Function call 
foo = generateRandomPoint(rangeInt) 
print (foo) 
file = open("turtle.py","w")
file.write(str(foo))
file.close()

# # Python3 program to generate 
# # a random function which generates 
# # float point in double list 
  
# # Function to generate float points 
# # Type is required as we need to return 
# # float in a list 
# def generateRandomFloatPoint(): 
#     global Type 
#     Type = float
  
#     # Generate random points 

