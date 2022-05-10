from bz2 import BZ2Decompressor
BZ2Decompressor()
from Bio import SeqIO
"""
KE downlaoded two files and unzipped them
/Users/karen/Documents/CSE-160/Zhou_Project/
ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/H_sapiens/mRNA_Prot/human.1.rna.fna.gz
~ / H_sapiens.fasta
"""

#downlaoded two files and unzipped them

from pathlib import Path
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


#function that takes in a fasta file and returns a SeqRecord
def get_seq(fasta_file):
    fasta = Path(fasta_file)
    if fasta.is_file():
        records = list(SeqIO.parse(str(fasta),"fasta"))
        return records
    else:
        print('fasta file not found')
        return None

def parse
