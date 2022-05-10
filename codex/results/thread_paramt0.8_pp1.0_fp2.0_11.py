import sys, threading
threading.Thread(target=lambda: sys.stderr.write(__file__.upper() + '\n')).start()

"""
FASTA file reader and writer
"""

from ..externals.six import print_


class Fasta(object):
    """FASTA entry reader.

    :param handle: the file-like handle
    :param default_seq_id: the default sequence ID (used when the read data has no ID)
    :param description_wrap: sequence description wrapping width (0: no wrapping)
    :param wrap: sequence data wrapping width (0: no wrapping)

    Usage::

        from Bio import SeqIO
        from Bio.Seq import Seq
        from Bio.SeqRecord import SeqRecord

        record = SeqRecord(Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF", IUPAC.protein),
                           id="YP_025292.1", name="HokC",
                           description="toxic membrane protein, small")

        print(SeqIO.read(open("Quality/
