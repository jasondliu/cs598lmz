import lzma
lzma_files = [f for f in os.listdir('./blobs') if '.xz' in f]
lzma_files

for f in lzma_files:
    with lzma.open('./blobs/'+f,'r') as source:
        with open('./blobs/'+f.split('.')[0],'wb') as dest:
            dest.write(source.read())

 
blob_files = [f for f in os.listdir('./blobs') if 'blob' in f]
blob_files

out_files = [f.split('.')[0]+'.npy' for f in blob_files]

for i in range(len(blob_files)):
    with gzip.open('./blobs/'+blob_files[i],'rb') as source:
        with open('./blobs/'+out_files[i],'wb') as dest:
            dest.write(source.read())




for i in range(10):
    print
