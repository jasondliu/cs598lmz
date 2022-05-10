import codecs
codecs.getwriter('utf-8')(sys.stdout)

from optparse import OptionParser
#from optparse import Option

from lxml import etree

from mapping import make_mapping
from transform import transform_xml
from graph import Graph
from relation import Relation

def main(argv, out=sys.stdout):
    parser = OptionParser("usage: %prog [options] file")
    parser.add_option("-m", "--mapping-file", dest="mapping",
            help="Load mapping from FILE.", metavar="FILE")
    parser.add_option("-o", "--output-file", dest="outfile",
            help="Write output to FILE.", metavar="FILE")
    #parser.add_option("-O", "--omit-empty", dest="omit", action="store_false", default=True,
    #        help="Omit the 'omit-empty' attribute.")
    parser.add_option("-p", "--plan", dest="plan",
            help="Use transformation plan from FILE.", metavar="
