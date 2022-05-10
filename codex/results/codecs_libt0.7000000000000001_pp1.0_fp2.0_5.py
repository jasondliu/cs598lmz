import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#import chardet
#df = pd.read_csv(r'C:\Users\kiwamiz\Desktop\kiwamiz\a.csv', encoding="ISO-8859-1")

#f_csv = pd.read_csv('C:\Users\kiwamiz\Desktop\kiwamiz\a.csv', encoding='cp932')

#print(f_csv)

#df = pd.read_csv(r'C:\Users\kiwamiz\Desktop\kiwamiz\a.csv', engine='python', encoding='cp932')

#print(df)

#coding: utf-8
import csv
# read csv file
csv_file = csv.reader(open('C:\Users\kiwamiz\Desktop\kiwamiz\a.csv',encoding='cp932'))

# skip the title line
header = next(csv_file)

for
