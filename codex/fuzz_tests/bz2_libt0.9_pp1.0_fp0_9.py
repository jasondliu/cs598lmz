import bz2
bz2_file = bz2.BZ2File('C:\Users\Administrator\Desktop\file_example_XLS_1000.xls.bz2')
data = bz2_file.read()
bz2_file.close()
with open('newfile.xls', 'wb') as f:
    f.write(data)
 
 
# 匹配
import re
re.findall('[0-9]+', 'hello 1234 this is egons book 87533')
 
# 贪婪匹配
re.findall('[0-9]*', 'hello 1234 this is egons book 87533')
# 非贪婪匹配
re.findall('[0-9]+?', 'hello 1234 this is egons 
 
print(re.findall('[0-9]+?', 'hello 1234 this is egons book 87533'))
print(re.findall('\w+?', 'hello 1234 this is egons book 875
