import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf-8mb4' else None)

class Ucsc:
    def __init__(self):
        self.conn = pymysql.connect(host='genome-mysql.cse.ucsc.edu', user='genome', password='', db='hg19', charset='utf8')
        self.cursor = self.conn.cursor()

    def get_genes_by_chromosome(self, chromosome):
        query = 'SELECT name FROM kgXref WHERE kgID like "NCBIGene:%" AND chrom like "%s"' % chromosome
        self.cursor.execute(query)
        genes = []
        for gene in self.cursor.fetchall():
            genes.append(gene[0])
        return genes

    def get_gene_locations_by_chromosome(self, chromosome):
        query = 'SELECT chromStart, chromEnd FROM kgXref WHERE kgID like "NCBIGene:%" AND chrom like "%s"' % chromosome
       
