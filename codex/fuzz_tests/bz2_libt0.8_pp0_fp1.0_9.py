import bz2
bz2_obj=bz2.BZ2File('bz2_file','w')
bz2_obj.write('This is a test string.')
bz2_obj.close()
import pickle
import pprint
t1=('this is a string','this is another string','this is a third string','this is a fourth string')
f=open('pickle_file','w')
pickle.dump(t1,f)
f.close()
pickle.dumps(t1)
f=open('pickle_file')
t2=pickle.loads(f.read())
print(t2)
import csv
f=open('csv_file','w')
writer=csv.writer(f)
writer.writerow(('number','number+2','number*2'))
for i in range(10):
    writer.writerow((i,i+2,i**2))
f.close()
f=open('csv_file')
reader=csv.reader(f)
for row in reader:
    print(row)
f.close()

