import bz2
bz2_f = bz2.BZ2File(path2, 'w')
bz2_f.write('FOOBARFOOBARFOOBAR'.encode())
bz2_f.close()

f = open(path3, 'wb')
f.write('FOOBARFOOBARFOOBAR'.encode())
f.close()

print(gzip.open(path1, 'r').read().decode())
print(bz2.BZ2File(path2, 'r').read().decode())
print(open(path3, 'rb').read().decode())

# gunzip-1.6.tar.gz
# result: File has been downloaded successfully.
# gunzip-1.6
# set up virtualenv
# result: Successfully installed virtualenv
# result: Successfully created virtual environment
# list of all files in virtualenv

# gunzip-1.6
# result: Installing setuptools, pip...done.
# result: Virtual environment is active.
# result: Successfully installed gunzip-1.6
