import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
with bz2.open("final_fasta.fasta.bz2", 'rb') as src, open("fasta_out.fasta", 'wb') as dest:
    for data in iter(lambda : src.read(20000), b''):
        dest.write(decomp.decompress(data))
%%time
with open("fasta_out.fasta", "r") as f:
    seq = f.read().replace("\n","")
kmers = kmers_from_file(seq, k)

def counts(kmers):
    count = Counter(kmers)
    return dict(count)

kmers_count = counts(kmers)
print('Total number of kmers:', len(kmers))
total_kmers = len(kmers)

# Get 20 kmers with the highest count.
kmers_count_top = dict(Counter(kmers_count).most_common(20))

# Get 20 kmers with the lowest count.
kmers_count_
