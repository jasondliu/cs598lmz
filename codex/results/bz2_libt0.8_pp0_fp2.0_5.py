import bz2
bz2_file = bz2.BZ2File(file_name)

# go through the bars one by one
for line in bz2_file:
    line = line.decode("utf-8")
    fields = line.split("\t")

    # check for empty lines
    if len(fields) < 3:
        continue
    
    # check for invalid field numbers
    if fields[0] != 'bar':
        continue
    
    # get the bar name
    bar_name = fields[2]
    
    # optionally print the bar name
    print(bar_name)
