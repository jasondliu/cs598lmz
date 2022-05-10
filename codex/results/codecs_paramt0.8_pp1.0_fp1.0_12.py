import codecs
codecs.register_error("strict", codecs.ignore_errors)

import gzip

def open(filename, mode="r"):
    if mode == "r" and filename.endswith(".gz"):
        return gzip.open(filename, mode=mode)
    else:
        return file(filename, mode=mode)

names = []
with open("titles.gz", mode="r") as f:
    results = []
    data_per_hit = []
    for line in f:
        if line.startswith("\t"):
            data_per_hit.append(line)
        else:
            if data_per_hit:
                results.append(data_per_hit)
            data_per_hit = []

    for title, hits in zip(results[::2], results[1::2]):
        title = title[0].decode("ascii", "strict").strip()
        hits = [h.decode("ascii", "strict").strip().split("|")
                for h in hits]
        names.append((
