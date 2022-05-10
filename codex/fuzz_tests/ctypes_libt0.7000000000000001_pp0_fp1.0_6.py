import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#Import the module os
import os
#Get the user profile
user = os.environ['USERPROFILE']
#Show the user profile
user

#Import the module os
import os
#Get the user profile
user = os.environ['USERPROFILE']
#Create a folder called "hello" inside the user profile
os.mkdir(user + "\hello")
print("Folder created successfully!")

#Import the module os
import os
#Get the user profile
user = os.environ['USERPROFILE']
#Create a folder called "hello" inside the user profile
os.mkdir(user + "\hello")
print("Folder created successfully!")
#Remove the folder "hello" inside the user profile
os.rmdir(user + "\hello")
print("Folder removed successfully!")

#Import the module os
import os
#Get the user profile
user = os.environ['USERPROFILE']
#Create a folder called "hello" inside the user profile
os.mk
