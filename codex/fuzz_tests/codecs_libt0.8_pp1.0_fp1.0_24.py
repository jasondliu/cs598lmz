import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# Open excel workbook
xlsx = pd.ExcelFile(r'C:\Python27\Scripts\ProdList.xlsx')

# Parse the first sheet and rename the columns
df = xlsx.parse(0)
df.rename(columns={
  'Product': 'Item',
  'Amount': 'Qty',
  'Name': 'Name'
}, inplace=True)

# Convert the pandas dataframe to a list of dictionaries (JSON)
records = df.to_dict('records')

# Convert the list of dictionaries to a JSON string
json_str = json.dumps(records, indent=2)

# Write the JSON string to a file
with open(r'C:\Python27\Scripts\ProdList.json', 'w') as f:
  f.write(json_str)
