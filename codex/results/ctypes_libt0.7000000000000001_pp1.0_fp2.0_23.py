import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
# https://stackoverflow.com/questions/4646946/how-to-display-an-error-message-box-using-tkinter

class Person:
    
    def __init__(self, fname, lname, age, gender, height, weight):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def say_hello(self):
        print("Hello, my name is " + self.fname + " " + self.lname)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.fname + " " + self.lname)
        
    def height_weight(self):
        return (str(self.height) + " inches" + " and " + str(self.weight) + " pounds")
        
    def bmi(self):
       
