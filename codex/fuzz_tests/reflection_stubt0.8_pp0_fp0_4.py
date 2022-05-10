fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()

print('')
print('############################### Try ##')
###################################################################
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print("Error: can\'t find file or read data")

print('')
print('############################### Try ##')
###################################################################
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")
   
print('')

