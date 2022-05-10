import bz2
# Test BZ2Decompressor at EOF
for FNAME in ../testdata/*.bz2; do
    echo ${FNAME##*../}
    BZ2_FNAME=${FNAME##*../}
    PY_FNAME=../testdata/py_${BZ2_FNAME}
    TF_FNAME=../testdata/tinybz2_${BZ2_FNAME}

    # Compare BZIP2 with the Pytho
