import bz2
bz2_file = bz2.BZ2File(download_link) # open the file
data = bz2_file.read() # get the decompressed data
new_file_path = download_link[:-4] # assuming the filepath ends with .bz2
open(new_file_path, 'wb').write(data) # write a uncompressed file
 
with open(new_file_path, 'rb') as f:
    csv_reader = csv.reader(f)
    data_list = list(csv_reader)

df = pd.DataFrame(data_list)
#df.columns = df.iloc[0]
#df = df[1:]
df[0] = df[0].astype(int)
df.info()

new_file_path = '../data/train.csv' # assuming the filepath ends with .bz2
with open(new_file_path, 'wb') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_list)
