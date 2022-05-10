from lzma import LZMADecompressor
LZMADecompressor().decompress(open(my_data_dir+"wiki/AA/wiki_00","rb").read())[:50]

clean_text=[]
for i in range(len(p_files)):
    print(i)
    in_file_name=my_data_dir+"wiki/"+p_files[i]
    clean_text.append(LZMADecompressor().decompress(open(in_file_name,"rb").read()))
    open(my_data_dir+"wiki/"+p_files[i]+".utf8","w").write(clean_text[i])

def wiki_dump_cleaner(path_in,path_out):
    clean_text=[]
    for i in range(len(p_files)):
        print(i)
        in_file_name=my_data_dir+"wiki/"+p_files[i]
        clean_text.append(LZMADecompressor().decompress(open(in_file_name,"rb").read()))
        open(path_out
