import ctypes
ctypes.cast(0, ctypes.py_object)

#Slicing Strings
str = 'X-DSPAM-Confidence: 0.8475'
str.find(':')

str[str.find(':')+2:]

#Problem 7.1
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Problem 7.2
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    words = line.split()
    print(words[1
