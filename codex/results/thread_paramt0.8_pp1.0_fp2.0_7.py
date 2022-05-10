import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from a thread!\n')).start()
 
# Some more Python 3.4 good stuff:
print (os.path.relpath('/app', '/app/e1/e2'))


# Some really old Python:
# print 'Hello World!'
# print 'Another way to print a string.'
# print 'A third way to print a string.'
# if 5 < 10:
# 	print 'Five is less than 10!'

# count = 1
# while count < 5:
# 	print count
# 	count = count + 1


# name = raw_input('Enter your name: ')
# if name == 'Chris':
# 	print 'Lucky you!'
# else:
# 	print 'Hello ' + name.title() + '!'
