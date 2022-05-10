import socket
socket.if_indextoname(1)

# Question 6
import os
os.getcwd()

# Question 7
import os
os.environ

# Question 8
import platform
platform.system()

# Question 9
import os
print("Current File Name : ",os.path.realpath(__file__))

# Question 10
import datetime
print("Current Date and Time : ",datetime.datetime.now())

# Question 11
import datetime
print("Current Date and Time : ",datetime.datetime.now().date())

# Question 12
import math
a = int(input("Enter the radius of the circle"))
print("The area of the circle is ",math.pi*a*a)

# Question 13
import random
a = random.randint(1,10)
print(a)

# Question 14
import random
a = random.randint(1,10)
b = int(input("Enter the number"))
if a==b:
	print("The number is guessed correctly")
else:
	print("The number is not guessed correctly")

# Question 15
