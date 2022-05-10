from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = BZ2Decompressor.decompress_python 
import os
import Theano
import optparse

import cPickle
from toolsdivers import *
import lasagne
from toolsTP import *



parser = optparse.OptionParser()

parser.add_option("--dossier", dest="dossier", default="/mnt/Data/RnD/Charles/CompGT/", help="dossier prepending")
parser.add_option("--dossierexec", dest="dossierexec", default="/triton/ics/project/imagedb/pipeline/NLMCXR_outer/execute/", help="dossier prepending")
parser.add_option("--nomexec", dest="nomexec", default="patchsVGGFordu13aug17", help="nom executable")
parser.add_option("--dossiersave", dest="dossiersave", default="/mnt/Data/RnD/Charles/CompGT/numeros", help="nom du fichier de sauvegarde")
parser.add_option("--re
