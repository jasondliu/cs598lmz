import codecs
codecs.register(ls.search_function)

import c3smembership.data.repository.offer_repository
import c3smembership.data.model.statistics.membership_list_stats
from c3smembership.business.invoicing import InvoiceParameter
from c3smembership.business.invoicing import RenewalInvoiceParameter
from c3smembership.business.invoicing import LatePaymentInvoiceParameter
from c3smembership.business.invoicing import NonPaymentRevocationInvoiceParameter
from c3smembership.business.invoicing import DebitNoteParameter
from c3smembership.business.invoicing import DebitNoteCancelParameter
from c3smembership.business.invoicing import GrantInvoiceParameter


class TestInvoicing(unittest.TestCase):
    """
    Test the invoicing utility.

    This test suite tests the invoicing utility functinality.
    It tests whether a certain invoice has been created.
    It tests whether a certain
