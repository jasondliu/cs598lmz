import bz2
bz2.decompress(s)
 

#Printing a single line from a file
with open('text.txt') as f:
    for line in f:
        print(line)


#Printing a single line from a file
with open('text.txt','r') as f:
    for line in f:
        print(line,end='')


#Reading a file in chunks
def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
            yield data

with open('text.txt', 'r') as f:
    for piece in read_in_chunks(f):
        process_data(piece)


#Writing a file in chunks
with open('/tmp/data.txt', 'w') as f:
    for piece in read_in_chunks(f):
        f.write(data)


#Reading a zip file
with zipfile.ZipFile('text.zip', 'r') as z:

