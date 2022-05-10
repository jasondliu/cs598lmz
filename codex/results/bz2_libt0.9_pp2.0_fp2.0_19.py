import bz2
bz2.open(Filename)

with open(Filename, 'wt', newline = '') as file:
	write = csv.writer(file)
	write.writerow(HeaderList)
	for i in FileList:
		write.writerow(i)
