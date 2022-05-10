import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def fichier_unique(fichier):
	mots = []
	with open(fichier, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			line = line.replace('\r', '')
			line = line.replace('  ', ' ')
			words = line.split(' ')
			for w in words:
				mots.append(w)
	return list(set(mots))

def create_dict(fiche_origine, fichier_clos):

	mots_u = fichier_unique(fichier_clos)

	vocabulaire = {}
	vocabulaire_rev = {}

	for mot in mots_u:
		vocabulaire[mot] = len(vocabulaire) + 1
		vocabulaire_rev[
