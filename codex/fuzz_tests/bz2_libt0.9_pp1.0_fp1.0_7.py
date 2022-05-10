import bz2
bz2.decompress(data)

gzipfile.open("./feature_perso_hash.h5", "rb") # returns a gzipfile object

with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()
    # decompress data from file_content

import shutil
shutil.unpack_archive('feature_perso_hash.h5', 'tmp/archive')

#for csv
liste_conso_little = []
liste_conso_little.append(liste_conso[-1])
import csv
with open(filepath_abs, "w") as fp: #opens csv file
    wr = csv.writer(fp, dialect='excel')
    wr.writerows(liste_conso_little)

#utile pour les graphiques
import matplotlib.pyplot as plt
import datetime

tableau_de_correspondance = {
    "enjeu_sources_renouvelables" : "sources_ren
