import gc, weakref
try:
	import cPickle as pickle
except ImportError:
	import pickle
from webnotes.model.doc import addchild
from webnotes.model.code import get_obj
from webnotes.utils import flt, set_max_length, cstr
from webnotes.model.doclist import getlist
from webnotes import msgprint, _
from setup.utils import get_company_currency

set = webnotes.conn.set
sql = webnotes.conn.sql
get_value = webnotes.conn.get_value
in_transaction = webnotes.conn.in_transaction
convert_to_lists = webnotes.conn.convert_to_lists
	
# -----------------------------------------------------------------------------------------


class DocType:
	def __init__(self, doc, doclist=[]):
		self.doc = doc
		self.doclist = doclist
		self.tname = 'Purchase Invoice Item'
		self.fname = 'entries'
		self.status_updater = [{
			'source_dt
