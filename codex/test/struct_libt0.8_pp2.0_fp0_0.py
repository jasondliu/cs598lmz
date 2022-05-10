import _struct
import array

from pyasn1.type import univ, tag, char, namedtype, namedval, tagmap, constraint
from pyasn1.codec.ber import eoo
from pyasn1.compat.octets import null

##
# Abstract Syntax Notation One (ASN.1) basic type library with BER codec.
#
# @see: http://luca.ntop.org/Teaching/Appunti/asn1.html
# @see: U{http://www.oss.com/asn1/resources/books-whitepapers-pubs/}
# @see: U{http://msdn.microsoft.com/en-us/library/windows/desktop/aa381058(v=vs.85).aspx}
# @see: RFC 1952 (GZIP file format specification version 4.3)
# @see: RFC 2045 (Multipurpose Internet Mail Extensions)
# @see: RFC 2046 (Media Types)
# @see: RFC 2233 (IANA Charset Registration Procedures)
