import _struct

#==============================================================================
class GenoTable(object):
    """Base class for a table containing a genotype matrix.

    A genotype table is a table of genotypes, loaded and stored as a dense
    numpy array in memory. GenotypeTable objects can be accessed either
    by indexing, or by an iterable (like a matrix). Methods can be
    applied to the GenoTable object in place, and all changes will be made
    to the underlying object, or changes can be made to a copy, leaving the
    original unaffected.

    """
    #--------------------------------------------------------------------------
    # Constructor.
    #--------------------------------------------------------------------------
    def __init__(self, geno, loci, individuals, major_allele=None,
            max_missing=None):
        """Create a new GenoTable object.

        If a major allele is not specified, one will be automatically
        determined.

        """
        # Create the table.
        geno = np.asarray(geno, dtype=np.uint8)

        # Validate the genotype array.
        if geno.ndim != 3:
