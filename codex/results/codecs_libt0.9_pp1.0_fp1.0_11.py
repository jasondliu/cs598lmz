import codecs
codecs.open('data/errors.txt', 'w', 'utf-8').writelines(errors)
 
os.system("rm data/tmp.*")
print('Total rows: {0}'.format(totalrows))
print('Done!')
