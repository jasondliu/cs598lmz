import bz2
bz2.BZ2File("./tmp/wikidata-20170306-all.json.bz2", "r")


import bz2
import json
import os
import shutil

def unpack_bz2(path, tmp_dir="./tmp"):
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    with bz2.BZ2File(path, "r") as f:
        with open(os.path.join(tmp_dir, "wikidata-20170306-all.json"), "w") as out:
            out.write(f.read())


def repack_bz2(path, tmp_dir="./tmp"):
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    with open(os.path.join(tmp_dir, "wikidata-20170306-all.json"), "r") as f:
        with bz2.BZ2File(path, "w
