import codecs
codecs.open('test.txt',encoding='utf-8')

import os
os.listdir('.')

import  glob
glob.glob('*.py')

import sys
sys.argv
sys.stderr.write('Warning, log file not found starting a new one\n')

#re
import re
re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1',r'\1','cat in the the hat')
'tea for too'.replace('too','two')

#math
import math
math.cos(math.pi/4)
math.log(1024,2)

import random
random.choice(['apple','pear','banana'])
random.sample(range(100),10)
random.random()
random.randrange(6)

import statistics
data=[2.75,1.75,1.25,0.25,0.5,1.25,3.5]
statistics.mean(
