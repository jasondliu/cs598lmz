import bz2
bz2.__path__

%run bz2_test.py
>&2 echo "bz2 tests done"

bzip2 -kv -z bz2_test.py
bzip2 -kv -z bz2_test.py

%run bz2_test.py
>&2 echo "bz2 tests done"

mkdir bz2test
cd bz2test
cp ../bz2_test.py .
time bzip2 -z -k bz2_test.py
cp ../bz2_test.py .
time bzip2 -z -k bz2_test.py
cp ../bz2_test.py .
time bzip2 -z -k bz2_test.py
cp ../bz2_test.py .
time bzip2 -z -k bz2_test.py
cp ../bz2_test.py .
time bzip2 -z -k bz2_test.py
cp ../bz2_test.py .
time bzip2 -
