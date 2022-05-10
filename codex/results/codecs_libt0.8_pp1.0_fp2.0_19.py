import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import csv


csvfile = open(r'H:/P/PythonProgramming/2_DataAnalysis/1_PythonBasics/11_WorkingWithCSVAndJSON/sales.csv', 'rb')
csvReader = csv.reader(csvfile)
for row in csvReader:
	print row
csvfile.close()


# 2) Writing a csv file:

csvfile = open(r'H:/P/PythonProgramming/2_DataAnalysis/1_PythonBasics/11_WorkingWithCSVAndJSON/sales.csv', 'wb')
output = csv.writer(csvfile)
data = [['Me', 'You'],
		['293', '219'],
		['54', '13']]
output.writerows(data)
csvfile.close()


# 3) To write to a csv file, in a more user friendly format

csvfile = open(r'H:/P/PythonProgramming/2_
