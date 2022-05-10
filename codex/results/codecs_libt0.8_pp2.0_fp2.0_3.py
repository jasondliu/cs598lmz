import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Opens the file for reading. This is where you need to change the directory for data file.
with open('C:\\Users\\hsu\\Desktop\\SCM data\\BigData_V2\\Recommender_System\\RS_data\\test_set_V4.csv', 'r', newline='', encoding='utf-8-sig') as file_in:
    filereader = csv.DictReader(file_in, delimiter=',')
    for row in filereader:
        test_set.append(row)

##For removing the duplicated vehicle ID
#for i in range(len(test_set)):
#    if test_set[i]['vehicle_id'] == test_set[i-1]['vehicle_id'] and i > 0:
#        test_set.pop(i)

#Calculate the score
for i in range(len(test_set)):
    if test_set[i]['veh
