import select
import threading
import time

from ovs.db import error
from ovs.db import idl
from ovs.db import types


class IdlTransaction(object):
    def __init__(self, idl, dry_run=False):
        self.idl = idl
        self.dry_run = dry_run
        self.txn = None
        self.error = None
        self.seqno = None

    def __enter__(self):
        self.txn = self.idl.txn_create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.dry_run:
            self.idl.txn_destroy(self.txn)
        else:
            self.error, self.seqno = self.idl.txn_commit_block(self.txn)
            if self.error:
                raise RuntimeError("Transaction error: %s" % self.error)


class Idl(object):
    def __init__(self, schema
