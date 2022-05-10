import lzma
lzma.LZMAFile

print("Reading input data...")
with gzip.open(sys.argv[1], "rb") as f:
    data = pickle.load(f)

print("Reading existing data...")
with lzma.LZMAFile(sys.argv[0], "rb") as f:
    existing = f.read().decode("utf-8")

print("Writing new data...")
with lzma.LZMAFile(sys.argv[0], "wb") as f:
    f.write((existing + "\n" + json.dumps(data)).encode("utf-8"))

print("Done.")
