import codecs
codecs.open('test.txt', 'rb', 'utf8')

import os
os.mkdir('testDir')

import os
os.makedirs('testDir')

import os
os.makedirs('testDir/testDir2')

import os
os.rename('testDir','testDir2')

import os
os.rmdir('testDir2')

import os
os.removedirs('testDir2/testDir3')

import os
os.mkdir('testDir')
os.mkdir('testDir/testDir2')
os.rmdir('testDir/testDir2')
os.rmdir('testDir')

import os
os.rename('test.txt', 'test2.txt')

import os
os.remove('test2.txt')

import os
os.getcwd()

import os
os.chdir('/server/accesslogs')
os.getcwd()

import os
os.chdir('/home/chris')
os.getcwd()

import
