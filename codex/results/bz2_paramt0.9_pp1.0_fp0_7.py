from bz2 import BZ2Decompressor
BZ2Decompressor()

# print((os.listdir('.')))
%cd data_combined

download('t3.micro', '100', '100')
download('t3.micro', '100', '180')
download('t3.micro', '100', '300')
download('t3.micro', '100', '500')
download('t3.micro', '100', '1000')
download('t3.micro', '100', '2000')
download('t3.micro', '100', '5000')

download('t3.large', '100', '020')
download('t3.large', '100', '040')
download('t3.large', '100', '080')
download('t3.large', '100', '160')
download('t3.large', '100', '320')

download('m4.xlarge', '100', '020')
download('m4.xlarge', '100', '080')
download('m4.xlarge', '100', '160')

download('m4.2xlarge', '100', '040')
download('
