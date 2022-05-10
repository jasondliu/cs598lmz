import lzma
lzma_files = [file for file in os.listdir('.') if file.endswith('.xz') ]
output = "."
for a in lzma_files:
    archive = lzma.LZMAFile(a)
    basename = os.path.basename(a).rstrip('.tgz')
    if not os.path.exists(output+"/"+basename):
        os.makedirs(output+"/"+basename)
    filename_out = os.path.join(output, basename, basename+'.rds')
    with open(filename_out, 'wb') as fout:
        print(filename_out)
        shutil.copyfileobj(archive, fout)
    del archive
    
    

#for fn in os.listdir('.'):
#    if fn.endswith('zip'):
#        outfile = fn.split('.')[0]
#        with zipfile.ZipFile(fn, 'r') as zip_ref:
#            zip_ref.extractall('
