import bz2
bz2.decompress(packed)

# C'era un b al punto 8 (bz2) che non avevo notato subito e una volta trovato non so come si potesse risalire ad esso
# Parecchie pagine di thread di vari metodi di sblocco del telefono tra cui questa:
# http://forum.xda-developers.com/showthread.php?t=1309960
# Con dei trucchi per accesso visto che il telefono essendo Nokia e di qualche anno fa non aveva accesso alla shell
# di linux da cui fare l'informazione della password e dei file, ma serviva sapere il nome del file da sms.
# XDA mi ha ricordato che la password poteva esserci, ma non serve perché il file era aperto, pur bloccando lo sblocco
# ma con un altro file si può contattare il sito di xda che prova password dal dizionario. St
