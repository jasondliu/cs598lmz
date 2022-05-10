import codecs
codecs.register_error('replace_not_relevant_codes', ReplaceNotRelevantCodes())

stoplist = set('for a of the and to in'.split())

def desw_or_named(n):
	return 'desw' if n<=5 else 'named'

def tagged(category):
	return int(category.strip().split(',')[1])

def label(category):
	return category.strip().split(',')[0]

class TwitterCorpusReader():

	def __init__(self, root, limit_posts=False, limit_desw_named=False, stemmed=False, load_to_ram=False, load_separately=False):
		self.root = root
		self.pos_map = {'ADJ' : 'a', 'ADP' : 'i', 'ADV' : 'r', 'AUX' : 'v', 'CONJ' : 'c', 
		'DET' : 'd', 'INTJ' : 'g', 'NOUN' : 'n', 'NUM' : 'm', 'PART' : '
