import codecs
codecs.register_error("strict", codecs.ignore_errors)

class Breakdown(object):
    """This class contains the processing for ICD Breakdown

    @param padicd10: ICD-10 code hint
    @type padicd10: C{of.ICDCode}
    @param patabcd: ICD-10 Code Tab
    @type patabcd: C{ICDCodeTable}
    @param db: database connection
    @type db: C{misc.dbconnection}
    @param ghd: droit d'accès
    @type ghd: C{vlist.GHDroit}
    @param pabd: breakdown
    @type pabd: C{of.ICDCode}
    """

    def __init__(self, padicd10, patabcd, db, ghd, pabd=None):
        """Constructor
        """

        self.padicd10 = padicd10
        self.lstbcds = [self.padicd10]
        self.tabicd10 = patabcd
        self.db
