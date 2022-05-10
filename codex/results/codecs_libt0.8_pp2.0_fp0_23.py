import codecs
codecs.open('subsample.txt','w','utf_8').write(subsample)

# subsample
subsample = ','.join(subsample.split('\n'))
subsample = subsample.split(',')
subsample.pop(-1)


# make list of features
import numpy as np
subsample = np.random.choice(subsample, size=len(subsample)//2, replace=False)
subsample = ','.join(subsample)
subsample = subsample.replace(',','\n')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
subsample = subsample.replace('  ',' ')
sub
