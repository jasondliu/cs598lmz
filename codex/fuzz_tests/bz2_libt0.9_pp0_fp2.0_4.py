import bz2
bz2_count=0
bz2_info=[]
with bz2.open('bookings.csv.bz2') as bz_csv:
    for row in bz_csv:
        a=row.split(',')[1]
        b=row.split(',')[2]
        if a!="":
            if a[0]=='"':
                idx_quote=a.find('"', 1)
                iata_scelta=a[1:idx_quote]
                #print a, iata_scelta
            else: iata_scelta=a[0:3]
            if iata_scelta=='MAD': 
                bz2_info.append(b)
                bz2_count+=1
print bz2_count
sum(1 for row in bz2_info)
with open('bookings.csv', 'r') as load_csv:
    csv_count=0
    for row in csv.reader(load_csv, delimiter='^'):
