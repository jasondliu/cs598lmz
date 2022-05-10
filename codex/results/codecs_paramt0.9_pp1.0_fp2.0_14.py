import codecs
codecs.register_error("strict", codecs.ignore_errors)

# def run():
    
pythonList= ["family.py","fridge.py","home.py","movies.py","music.py","to_do.py"]
#""""
myClassList=[]


for x in pythonList:
    os.system('python {p}'.format(p=x))
    a=x.split(".")
    myClassList.append(a[0])
    
    
    
    
    
print myClassList
#"""


for y in myClassList:
    print ("import {0};".format(y))
    x= __import__(y)
    print x

# for list in myClassList:


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""

