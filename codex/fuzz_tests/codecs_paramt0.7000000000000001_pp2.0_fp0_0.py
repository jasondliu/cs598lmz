import codecs
codecs.register_error('strict', codecs.replace_errors)

import re
import subprocess

fn = 'hg19_refGene.txt'

to_remove = 1000

# get all transcripts
transcripts = {}
with open(fn, 'r') as f:
    for line in f:
        parts = line.split('\t')
        transcripts[parts[1]] = parts[0]

# for each transcript, get the number of sequences in the fasta file
with open(fn, 'w') as out:
    for t in transcripts:
        seq = subprocess.check_output(['hgsql', 'hg19', '-e', 'select seq from %s' % t])
        seq = seq.decode('utf-8', 'strict')
        seq = seq.strip()
        seq = re.sub('[\n\r]', '', seq)
        seq = seq[:-to_remove]
        out.write('>%s\n%s\n' % (t, seq))
