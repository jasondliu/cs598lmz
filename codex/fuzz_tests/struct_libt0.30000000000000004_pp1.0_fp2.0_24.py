import _struct

from . import _common
from . import _compat
from . import _errors
from . import _util
from . import _vendor
from . import _x509
from . import backend

__all__ = [
    "Certificate",
    "CertificateSigningRequest",
    "CertificateRevocationList",
    "load_pem_x509_certificate",
    "load_pem_x509_csr",
    "load_pem_x509_crl",
    "load_der_x509_certificate",
    "load_der_x509_csr",
    "load_der_x509_crl",
    "load_pem_x509_trust_list",
    "load_der_x509_trust_list",
]


def _obj2txt(backend, obj):
    bio = backend._new_mem_buf()
    backend._lib.PEM_write_bio_X509(bio, obj)
    return backend._bio_to_string(bio)


def _txt
