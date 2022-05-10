import codecs
codecs.lookup('my_encoding')

#loading the data 
file = codecs.open("C:\\Users\\kdusiu01\\Desktop\\Neuro2.txt", encoding='my_encoding')
data = pd.read_csv(file)
print(data)

#after the pattern is found we print it
for match in pattern.finditer(data):
    print('Found on:', match.start(), match.end())
</code>

