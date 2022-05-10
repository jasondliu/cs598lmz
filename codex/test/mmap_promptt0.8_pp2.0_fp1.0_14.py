import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
def snp_freq_calc(filename):
    dict = {}
    file = open(filename, 'r+')
    mm = mmap.mmap(file.fileno(),0)
    for line in iter(mm.readline, ''):
        if ">" in line:
            continue
        line = line.strip('\n')
        for i in range(len(line)-4):
            kmer = line[i:i+5]
            if (dict.get(kmer) == None):
                dict[kmer] = [0,0]
            dict[kmer][0] += 1
    mm.seek(0)
    for line in iter(mm.readline, ''):
        if ">" in line:
            continue
        line = line.strip('\n')
        for i in range(len(line)-4):
            kmer = line[i:i+5]
            temp_list = list(kmer)
