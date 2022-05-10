import bz2
bz2_file = bz2.BZ2File('./ipg140107.xml.bz2')
xml_content = bz2_file.read().decode()

# print(xml_content)

# Extract the patent classifications
classification_regex = re.compile(r'<us-bibliographic-data-grant><classifications-ipcr><classification-ipcr>([\w-]+)</classification-ipcr></classifications-ipcr></us-bibliographic-data-grant>')

all_classifications = classification_regex.findall(xml_content)

# print(all_classifications)

# Classify the classifications
classification_counter = Counter(all_classifications)

# print(classification_counter)

# Convert to a dataframe
classification_df = pd.DataFrame.from_dict(classification_counter, orient='index').reset_index()

classification_df.columns = ['Classification', 'Count']

# Print the dataframe
print(classification_
