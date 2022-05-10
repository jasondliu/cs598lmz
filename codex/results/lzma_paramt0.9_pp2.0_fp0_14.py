from lzma import LZMADecompressor
LZMADecompressor().decompress(chunk)

""" On average, it requires ~844 bits to encode a text string as a DNA
sequence """
def build_codec_dict(minbits, maxbits, encode=True):  
    """ build a codec dictionary using the DNA alphabet """
    base_power = 4
    pow_sequence = range(minbits, maxbits+1)
    sym_count = [base_power**p for p in pow_sequence]
    # redo to include degeneracy
    base_dict = {'A':0, 'T':1, 'G':2, 'C':3, 'N':4}
    c = 0
    if encode:
        dna_dict = {}
        for p in pow_sequence:
            strs = [''.join([k]*(p-1)) for k in base_dict.keys() if k <> 'N']
            for s in strs:
                for k in base_dict.keys():
                    if k <> 'N':
                        s2 = k+s
                        dna_dict[s2] = c
                       
