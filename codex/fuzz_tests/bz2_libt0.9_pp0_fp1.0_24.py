import bz2
bz2.block_size = 9

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    MRWordFreqCount.run()
!python WordCount_Assignment.py data/books/dearzoo.txt > test
# run python in terminal

!python WordCount_Assignment.py -r local data/books/dearzoo.txt

!python WordCount_Assignment.py -r local data/books/dearzoo.txt | sort -k2,2n -r | head
!python WordCount_Assignment.py data/books > dearzoo.counts
!python WordCount_Assignment.py data/books | sort -k2,2n -r >
