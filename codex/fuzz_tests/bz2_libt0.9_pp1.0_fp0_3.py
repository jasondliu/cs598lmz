import bz2
bz2.open('files.tar.bz2')

#create a new directory "target"
'''
import os
os.mkdir('target')

#using if condition with main
import sys
if __name__ == '__main__':
        print 'This program is being run by itself'
else:
        print 'I am being imported from another module'

# Make a script both importable and executable
'''
def main():
        print 'This program is being run by itself'
if __name__ == '__main__':
        main()
'''


'''
#sysargv command
import sys
print 'This is the name of this program:', sys.argv[0]
print 'Number of arguments:', len(sys.argv)
print 'Arguments:', str(sys.argv)
'''


#remove a file
#import os
#os.remove('filename')
#os.rename('oldname', 'newname')

'''
#open a file and print it
filename = raw_input('Enter the file name: ')

