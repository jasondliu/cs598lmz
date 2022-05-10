import socket


# Create a file object with write permission
f = open('./List_of_City_Name_State.txt', 'w+')

r = cities.stream(format='jsonl', force_xlsx=True, query={
    'limit': 10000,
    'country': 'US'})

for items in r:
    print(items.get('city'), items.get('admin1_code'))
    f.write("%s\t%s\n" % (items.get('city'), items.get('admin1_code')))

f.close()
