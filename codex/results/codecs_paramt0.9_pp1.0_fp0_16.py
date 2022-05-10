import codecs
codecs.register_error('ignore', codecs.replace_errors('<EOT>'))

import nltk

from nltk.tokenize import RegexpTokenizer

EPITOME_GLOSS_PATH = '../epitome_gloss.txt'
EPITOME_PATH = '../epitome_lex.txt'
EPITOME_TAGGED_PATH = '../epitome_lex.tagged.txt'
EPITOME_DICO = '../epitome.dico'

#==============================================================================
# Command line options
#==============================================================================

op = optparse.OptionParser()
op.add_option("-r", "--raw", action='store_true',
              default=False, help=u"Autorise les mots inconnus.")
op.add_option("-p", "--possible", action='store_true',
              default=False, help=u"Autorise les mots possibles")
op.add_option("-c", "--correction", action='store_true',
              default=False, help=u"Affic
