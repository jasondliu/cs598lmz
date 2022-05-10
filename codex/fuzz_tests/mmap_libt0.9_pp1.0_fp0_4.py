import mmap  # per inserire n sq
import csv   # per caricare info csv
 
# inizializzo i contatori per ciascun paziente
count = [0,0,0,0,0,0,0,0]
count2 = [0,0,0,0,0,0,0,0]

# apro il file csv con le descrizioni = le chiavi per la comprensione del codice
with open('codiciAlgos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)    
    for row in rows:
        if row['codice'] == 'ENVTR':
            print(row['descrizione'])

# apro il file csv con i codici = i codici che devo trovare e contare nel file sq
with open('condizioni_ricerca.csv') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    rows2
