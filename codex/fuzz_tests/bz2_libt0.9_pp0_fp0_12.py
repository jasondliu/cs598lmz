import bz2
bz2_file = bz2.BZ2File(BZ2_FILE)
 
time_spent = 0
content = u''
for i, line in enumerate(bz2_file):
    content += line.decode('utf-8')

now = datetime.datetime.now()
    
print("Time spent =", now - d1)
