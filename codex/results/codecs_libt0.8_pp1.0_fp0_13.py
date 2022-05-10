import codecs
codecs.open("nouveau_fichier.txt","w",encoding="utf-8").write("Ceci est un texte avec des accents")


# In[8]:

#Lire un fichier en utf-8

fichier = codecs.open("nouveau_fichier.txt","r",encoding="utf-8")

print(fichier.read())
fichier.close()


# In[9]:

#Détecter l'encodage d'un fichier

import chardet
fichier=open("nouveau_fichier.txt","rb")
print(chardet.detect(fichier.read()))


# In[ ]:
