import mmap
import sys
import glob
import os

def doc2mecab(doc_tokens, file_path):
	with open(file_path, 'w') as f:
		f.write('\n'.join(doc_tokens))
		f.write('\nEOS\n')
		#f.write('\n')

		#f.write('EOS\n')
		#print('\n'.join(doc_tokens))
		#print('EOS\n')
		#print()
	os.system('./mecab_devel_mecab -Owakati -b 512 < %s > %s.mecab' % (file_path, file_path))

	with open('%s.mecab' % file_path) as f:
		tokens = f.read()
		
	os.remove(file_path)
	os.remove('%s.mecab' % file_path)
	return tokens


def doc2tokens(
