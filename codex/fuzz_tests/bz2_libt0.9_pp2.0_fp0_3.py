import bz2
bz2_file = bz2.BZ2File('enwik8')

max_file = FileReader('max.csv.bz2')
avg_file = FileReader('avg.csv.bz2')
min_file = FileReader('min.csv.bz2')

max_list = max_file.readlines()
avg_list = avg_file.readlines()
min_list = min_file.readlines()

bz2_list = []
while (1):
   data = bz2_file.readline()
   if (len(data) < 1):
      break
   bz2_list.append(data)
   if (len(bz2_list) == len(max_list)):
      break

max_list = max_list[1:43224 + 1]
avg_list = avg_list[1:43224 + 1]
min_list = min_list[1:43224 + 1]

bz2_list_fixed = []
for x in bz2_list:
   x
