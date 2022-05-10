import bz2
bz2.open("./pisa2012.csv.bz2","r")

import pandas as pd
df = pd.read_csv("./pisa2012.csv.bz2", sep='\t')
len(df)
df.info() ## verifiez la taille du dataset, le nombre d'attributs, leurs type, si il y a des valeurs manquantes:
df.head()
df.dtypes
len(pd.unique(df["CNT"]))

# On peut afficher les statistiques descriptives par colonne avec "describe"
print (df.describe())

# Afficher les valeurs de chaque colonne
print ("CNT","ST01Q01","ST02Q01","ST46Q01","ST46Q02","ST46Q03","ST46Q04","ST46Q05","ST46Q06","ST46Q07","ST46Q08","ST46Q09","ST46Q10","ST46Q11","ST46Q12","ST46Q13")

# On peut
