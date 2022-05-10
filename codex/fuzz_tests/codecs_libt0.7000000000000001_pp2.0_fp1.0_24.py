import codecs
codecs.open('testfile.txt', mode='r', encoding='utf-8')

# To be safe we should always open files this way
with codecs.open('testfile.txt', mode='r', encoding='utf-8') as f:
    print(f.read())

# Writing to a file
f1 = codecs.open('testfile2.txt', mode='w', encoding='utf-8')

# OBS! This will overwrite any text in the file!
f1.write(u'Test\n')
f1.close()

# This will append to the file
f2 = codecs.open('testfile2.txt', mode='a', encoding='utf-8')
f2.write(u'Test 2\n')
f2.close()

with codecs.open('testfile2.txt', mode='r', encoding='utf-8') as f:
    print(f.read())

# The with statement is preferred because it automatically closes the file
# when it is done

# The with statement is preferred because it automatically closes the file
# when it
