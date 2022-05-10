import codecs
codecs.open(url, "r", "utf-8")

r = tabula.read_pdf(url,pages='all', stream=True)
data = []
for i in range(len(r)):
    data.append(r[i].to_json(orient='records', date_format='iso'))
    
output = []
for i in range(len(data)):
    for j in json.loads(data[i]):
        output.append(j)
        
df = pd.DataFrame(output)
df.drop(['areaCode','ref'], axis=1, inplace=True)
df.fillna(value=np.nan, inplace=True)
df.rename(columns={'areaName': 'Neighborhood'}, inplace=True)

#Get text to look through
finalList = []
#PDFMAILER
rows = range(len(df['Neighborhood'][:-1]))
for i in rows:
    try:
        finalList.append(df['Neighborhood'][i] + "-"
