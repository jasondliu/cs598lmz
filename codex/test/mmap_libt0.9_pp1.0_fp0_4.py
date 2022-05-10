import mmap  # per inserire n sq
import csv   # per caricare info csv
 
# inizializzo i contatori per ciascun paziente
count = [0,0,0,0,0,0,0,0]
count2 = [0,0,0,0,0,0,0,0]

# apro il file csv con le descrizioni = le chiavi per la comprensione del codice
with open('codiciAlgos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)    
