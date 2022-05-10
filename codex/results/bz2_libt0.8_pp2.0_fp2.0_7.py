import bz2
bz2.decompress(rows[0]).decode('utf-8')

for line in rows[:10]:
    print(bz2.decompress(line).decode('utf-8'))

rows[0]
# >>>>> 2.5 Write CSV Files <<<<<
names = ['Arya', 'Samson', 'Dora', 'Timon']
scores = [98, 95, 88, 78]
students = zip(names, scores)

with open('students.csv', 'w') as f:
    write = csv.writer(f)
    for student in students:
        write.writerow(student)


with open('students.csv', 'w') as f:
    write = csv.writer(f, delimiter=';', lineterminator='\n\n')
    for student in students:
        write.writerow(student)


with open('students.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter=';', lineterminator='\n\
