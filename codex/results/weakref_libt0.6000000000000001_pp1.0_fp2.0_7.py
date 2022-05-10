import weakref

from datetime import datetime, timedelta

from indy import ledger, error

from indy.error import ErrorCode

from indy.ledger import build_get_revoc_reg_def_request, \
    build_get_revoc_reg_request, build_get_revoc_reg_delta_request, \
    build_revoc_reg_entry_request, build_revoc_reg_def_request, \
    build_revoc_reg_entry_request

from indy.pool import set_protocol_version

from plenum.common.constants import TXN_TYPE, DATA, REVOC_REG_DEF, \
    REVOC_REG_ENTRY, REVOC_TYPE, ISSUANCE_BY_DEFAULT, ISSUANCE_ON_DEMAND, \
    REVOC_REG_DEF_ID, REVOC_TYPE, MAX_CRED_NUM, TAILS_HASH, TAILS_LOCATION, \
    REVOC_REG_DEF_TYPE, VALUE, ISSUED, REVOK
