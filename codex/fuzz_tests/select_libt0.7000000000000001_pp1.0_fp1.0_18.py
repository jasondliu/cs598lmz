import select_data
import os
import sys

c=select_data.main(sys.argv[1])
res=c.select_data()
print res
os.putenv("RES",res)
#print os.environ["RES"]
