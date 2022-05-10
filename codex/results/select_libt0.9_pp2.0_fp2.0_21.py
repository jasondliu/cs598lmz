import selectNPunctualHits as snp
import re
from argparse import ArgumentParser


def main(args):
    f = open(args.input)  # File with multiple hits

    summaryFile = open(args.summ, "w")
    hit_accession_to_description = {}

    for l in f:
        m = re.match('Query= (\S+)', l)
        if m:
            query_id = m.group(1)
            continue
        m = re.match('\s*(\S+) \(\d+\)', l)
        if m:
            # print query_id, m.group(1), hit_accession_to_description[m.group(1)]
            summaryFile.write('{0}\t{1}\t{2}\n'.format(
                query_id, m.group(1), hit_accession_to_description[m.group(1)]))
            continue
        m = re.match('> (\S+)', l)
        if m:
            summaryFile.write('\t{0}\t{
